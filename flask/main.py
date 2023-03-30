import os
import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request

import logging
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data import db_session
from data.users import Users
from forms.loginform import LoginForm
from forms.post_form import PostForm
from forms.registerform import RegisterForm
from VK import vk_main

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mega_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(Users).get(user_id)


@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    db_sess = db_session.create_session()
    if form.validate_on_submit():
        if db_sess.query(Users).filter(Users.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пользователь с таким email уже существует")
        if db_sess.query(Users).filter(Users.name == form.username.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пользователь с таким логином уже существует")
        user = Users(
            email=form.email.data,
            name=form.username.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        print(
            form.email,
            form.username,
            form.password,
            form.check_password,
            sep="\n"
        )
        return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Users).filter(Users.name == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/success')
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/success')
def success():
    return render_template('success.html', title='Успех')


@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        logging.warning(form.data)
        id = form.id.data
        tag = form.tag.data
        images = list()
        # images = form.images.data
        # raw_images = request.files.getlist(form.images.name)
        raw_images = form.images.data
        for raw_image in raw_images:
            image = raw_image.stream.read()
            images.append(image)
            # logging.warning(image)
        # logging.warning(images)
        start_on = form.start_on.data
        interval = form.interval.data
        posts = vk_main.create_posts(os.getenv('VK_ACCESS_TOKEN'), images, id, start_on, interval)
        for post in posts:
            post.post()
        logging.warning("POSTED!!!!")
        # logging.warning(id, type(id))
        # logging.warning(tag, type(tag))
        # logging.warning(images, type(images))
        # logging.warning(start_on, type(start_on))
        # logging.warning(interval, type(interval))
        # vk_main.create_post(os.environ.get('VK_ACCESS_TOKEN'), owner_id=id, from_group="1", message="aaaa")
        # vk_main.create_post(os.environ.get('VK_ACCESS_TOKEN'), "-219613882", "1", "aaaa")
        return render_template('success.html', title='Успех')
    # return f"{current_user.name}"
    return render_template('post.html', title='Пост', form=form)


if __name__ == "__main__":
    load_dotenv('.env')
    db_session.global_init()
    db_sess = db_session.create_session()
    # bot.start_bot()
    app.run(host="0.0.0.0", port=3000, debug=True)
