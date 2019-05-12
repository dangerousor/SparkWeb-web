#!/usr/bin/python
# -*- coding:utf-8 -*-
import json

from flask import Flask, jsonify, request, url_for, redirect
from flask_login import login_user, login_required, logout_user, current_user
from flask_mako import render_template

import task
from ext import db, mako, login_manager, LoginForm, RegisterForm
from models import DBData, DBUser, FlaskUser, DBTask

app = Flask(__name__, template_folder='templates',
            static_folder='static')
app.config.from_object('config')
app.secret_key = b'\x92\x86\xe8\xd3\xbdU\x93\xe6\xec\xebo\xe4\xe0l\xfb\x1c'

mako.init_app(app)
db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user_obj = DBUser.query.get(user_id)
    if user_obj:
        curr_user = FlaskUser()
        curr_user.id = user_id
        curr_user.username = user_obj.user_id
        return curr_user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = DBUser.query.filter(DBUser.user_id == username).first()
        if user and password == user.password:
            curr_user = FlaskUser()
            curr_user.id = user.index
            curr_user.username = username

            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user)

            return jsonify({
                'status': 0,
                'message': None,
            })
        else:
            if not user:
                return jsonify({
                    'status': 1,
                    'message': '用户名不存在',
                })
            else:
                return jsonify({
                    'status': 1,
                    'message': '密码错误',
                })
    # GET 请求
    else:
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return render_template('login.html', form=login_form)


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        return jsonify({
            'status': 0,
        })


@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = DBUser.query.filter(DBUser.user_id == username).first()
        if user:
            return jsonify({
                'status': 1,
                'message': '用户名已经注册',
            })
        db.session.add(DBUser(
            user_id=username,
            password=password,
        ))
        curr_user = FlaskUser()
        curr_user.id = DBUser.query.filter(DBUser.user_id == username).first().index
        curr_user.username = username
        login_user(curr_user)
        return jsonify({
            'status': 0,
            'message': None,
        })
    # GET 请求
    else:
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return render_template('register.html', form=register_form)


@app.route('/')
@login_required
def index():
    return render_template('index.html')
    # return 'Hello World!'


@app.route('/data/<ind>', methods=['GET'])
@login_required
def data(ind):
    return render_template('data.html', index=ind)


@app.route('/log/<task_id>', methods=['GET'])
@login_required
def log(task_id):
    res = DBTask.query.filter(DBTask.id == task_id).first()
    if not res:
        return 'Invalid!'
    else:
        if not res.log:
            return 'Empty'
        else:
            return res.log


@app.route('/sample', methods=['POST'])
@login_required
def sample():
    req = request.get_data().decode()
    req = json.loads(req)
    rows = DBData.query.filter(DBData.task_id == req['index']).all()
    # print(rows)
    return jsonify({
        'row': len(rows),
        'data': [[row.step, ] + eval(row.data) for row in rows],
    })


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# app.register_blueprint(model.bp)
app.register_blueprint(task.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9990, debug=True)
