import datetime
import sqlalchemy
from flask_login import UserMixin
from db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = "users"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.Text, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    tg_id = sqlalchemy.Column(sqlalchemy.Text, unique=True)
    created_at = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    vk_access_token = sqlalchemy.Column(sqlalchemy.Text)
