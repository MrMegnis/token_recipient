from flask import Flask
from tg import bot

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


if __name__ == "__main__":
    bot.start_bot()
    app.run()