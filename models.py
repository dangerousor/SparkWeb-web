#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask_login import UserMixin

from ext import db


class DBTask(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    subtime = db.Column(db.DateTime, nullable=False)
    endtime = db.Column(db.DateTime)
    status = db.Column(db.TEXT, nullable=False)
    task = db.Column(db.TEXT, nullable=False)
    user = db.Column(db.INT, nullable=False)
    title = db.Column(db.TEXT)
    note = db.Column(db.TEXT)
    log = db.Column(db.TEXT)
    is_deleted = db.Column(db.BOOLEAN, default=False)


class DBData(db.Model):
    __tablename__ = 'data'

    index = db.Column(db.INT, primary_key=True, autoincrement=True)
    task_id = db.Column(db.INT)
    step = db.Column(db.TEXT)
    data = db.Column(db.TEXT)


class DBUser(db.Model):
    __tablename__ = 'user'

    index = db.Column(db.INT, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.TEXT, nullable=False)
    username = db.Column(db.TEXT)


class FlaskUser(UserMixin):
    username = str()
    pass
