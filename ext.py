#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
from flask_mako import MakoTemplates
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import validators
from wtforms import widgets
from const import REDIS_DB, REDIS_PORT, REDIS_HOST


rd = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
mako = MakoTemplates()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'


class LoginForm(FlaskForm):
    username = StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=3, max=12, message='用户名长度3-12'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    password = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    submit = SubmitField(
        label='登陆',
        widget=widgets.SubmitInput(),
        render_kw={'class': 'btn-primary'}
    )


class RegisterForm(FlaskForm):
    username = StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    password = PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
    password2 = PasswordField(
        label='再次输入密码',
        validators=[
            validators.DataRequired(message='不能为空.'),
            validators.EqualTo('password', '两次密码不一致.'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
    submit = SubmitField(
        label='注册',
        widget=widgets.SubmitInput(),
        render_kw={'class': 'btn-primary'}
    )
