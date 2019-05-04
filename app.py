#!/usr/bin/python
# -*- coding:utf-8 -*-
import json

from flask import Flask, jsonify, request
from flask_mako import render_template

import task
from ext import db, mako
from models import DBData

app = Flask(__name__, template_folder='templates',
            static_folder='static')
app.config.from_object('config')

mako.init_app(app)
db.init_app(app)


@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello World!'


@app.route('/data/<index>', methods=['GET'])
def data(index):
    return render_template('data.html', index=index)


@app.route('/sample', methods=['POST'])
def sample():
    req = request.get_data().decode()
    req = json.loads(req)
    rows = DBData.query.filter(DBData.task_id == req['index']).all()
    return jsonify({
        'data': [[row.step, ] + eval(row.data) for row in rows],
    })


# @app.route('/trainfile/<user>', methods=['GET'])
# def trainfile(user):
#     rows = DBTrainFile.query.filter(DBTrainFile.user == user).all()
#     namelist = []
#     for row in rows:
#         namelist.append(row.filename)
#     return jsonify({'fileNameList': namelist})
#
#
# @app.route('/testfile/<user>', methods=['GET'])
# def testfile(user):
#     rows = DBTestFile.query.filter(DBTestFile.user == user).all()
#     namelist = []
#     for row in rows:
#         namelist.append(row.filename)
#     return jsonify({'fileNameList': namelist})


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# app.register_blueprint(model.bp)
app.register_blueprint(task.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9990, debug=True)
