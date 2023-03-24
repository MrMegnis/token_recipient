from flask import Flask, render_template, redirect

# from tg import bot
from forms.loginform import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mega_secret_key'


@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == "__main__":
    # bot.start_bot()
    app.run(host="0.0.0.0", port=3000)
