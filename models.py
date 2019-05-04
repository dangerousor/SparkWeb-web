#!/usr/bin/python
# -*- coding:utf-8 -*-
from ext import db


# class DBModel(db.Model):
#     __tablename__ = 'model'
#
#     id = db.Column(db.INT, primary_key=True, autoincrement=True)
#     user = db.Column(db.String(16), nullable=False)
#     modelname = db.Column(db.String(128), nullable=False)
#     dataname = db.Column(db.String(128), nullable=False)
#     comment = db.Column(db.String(1024))
#     subtime = db.Column(db.DateTime, nullable=False)
#     endtime = db.Column(db.DateTime)
#     status = db.Column(db.INT)
#     category = db.Column(db.INT, nullable=False)
#     modelfile = db.Column(db.String(128))


class DBTask(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    subtime = db.Column(db.DateTime, nullable=False)
    endtime = db.Column(db.DateTime)
    status = db.Column(db.TEXT, nullable=False)
    task = db.Column(db.TEXT, nullable=False)
    user = db.Column(db.String(16), nullable=False)
    title = db.Column(db.TEXT)
    note = db.Column(db.TEXT)
#
#
# class DBTestFile(db.Model):
#     __tablename__ = 'testfile'
#
#     id = db.Column(db.INT, primary_key=True, autoincrement=True)
#     filename = db.Column(db.String(512), nullable=False)
#     user = db.Column(db.String(16), nullable=False)


class DBData(db.Model):
    __tablename__ = 'data'

    index = db.Column(db.INT, primary_key=True, autoincrement=True)
    task_id = db.Column(db.INT)
    step = db.Column(db.TEXT)
    data = db.Column(db.TEXT)


# class DBTrainFile(db.Model):
#     __tablename__ = 'trainfile'
#
#     id = db.Column(db.INT, primary_key=True, autoincrement=True)
#     filename = db.Column(db.String(512), nullable=False)
#     user = db.Column(db.String(16), nullable=False)
