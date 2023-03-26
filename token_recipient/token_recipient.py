import flask
import requests
from flask import request, jsonify
from sqlalchemy import update

from data import db_session
from data.users import Users

blueprint = flask.Blueprint(
    'token_recipient_api',
    __name__,
    template_folder='templates'
)

#https://oauth.vk.com/authorize?client_id=51593041&client_secret=9DqqHq7CTmThwEGyPEM2&redirect_uri=https://ca55-2a01-540-316-8000-716e-d8db-1cb3-805b.eu.ngrok.io/api/post_token&scope=friends&response_type=code&state="1"
@blueprint.route('/api/post_token', methods=["GET"])
def post_token():
    code = request.args.get("code")
    print(request, code)
    url = "https://oauth.vk.com/access_token"
    params = {
        "client_id" : "51593041",
        "client_secret" : "9DqqHq7CTmThwEGyPEM2",
        "redirect_uri" : "https://ca55-2a01-540-316-8000-716e-d8db-1cb3-805b.eu.ngrok.io/api/post_token",
        "code" : code
    }
    response = requests.get(url, params=params).json()
    print(response)
    # db_sess = db_session.create_session()
    # update(Users).where(Users.id == request["state"]).values(vk_access_token=request["access_token"])
    return "success, token: " + response["access_token"]


@blueprint.route('/api/get_token/<int:user_id>', methods=["GET"])
def get_token(user_id):
    return "token"