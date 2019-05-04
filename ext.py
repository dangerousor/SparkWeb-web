#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
from flask_mako import MakoTemplates
from flask_sqlalchemy import SQLAlchemy

rd = redis.Redis(host='localhost', port=6379, db=0)
mako = MakoTemplates()
db = SQLAlchemy()
