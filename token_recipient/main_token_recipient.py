from dotenv import load_dotenv
from flask import Flask
import token_recipient

from data import db_session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mega_secret_key'




if __name__ == "__main__":
    load_dotenv('.env')
    db_session.global_init()
    app.register_blueprint(token_recipient.blueprint)
    app.run(host="0.0.0.0", port=3001, debug=True)
