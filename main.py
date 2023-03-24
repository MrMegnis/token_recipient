from flask import Flask
# from tg import bot
from dotenv import load_dotenv
from data import db_session

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


if __name__ == "__main__":
    load_dotenv('.env')
    db_session.global_init()
    db_sess = db_session.create_session()
    # bot.start_bot()
    app.run()
