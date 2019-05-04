# #!/usr/bin/python
# # -*- coding:utf-8 -*-
import json
import time

from flask import Blueprint, request, jsonify

from ext import rd, db
from models import DBTask

bp = Blueprint('model', __name__, url_prefix='/task')


@bp.route('/run/<user>', methods=['POST'])
def run(user):
    if request.method == 'POST':
        now = time.localtime(time.time())
        data = request.get_data().decode()
        # print(data)
        data = json.loads(data)
        try:
            db.session.add(DBTask(
                user=user,
                subtime=now,
                status="Ready",
                task=data['data'],
                title=data['title'],
                note=data['note'],
            ))
            # db.session.commit()
            row = DBTask.query.filter(DBTask.user == user, DBTask.subtime == now).first()
            task_id = str(row.id)
            rd.rpush('task', task_id)
            return jsonify({'status': 1})
        except:
            return jsonify({'status': -1})


@bp.route('/<user>', methods=['GET'])
def task(user):
    rows = DBTask.query.filter(DBTask.user == user).all()
    result = {'size': len(rows)}
    content = []
    for row in rows:
        tmp = dict()
        tmp['submitTime'] = row.subtime
        tmp['endTime'] = row.endtime
        tmp['status'] = row.status
        tmp['task'] = row.task
        tmp['id'] = row.id
        tmp['title'] = row.title
        tmp['note'] = row.note
        content.append(tmp)
    result['content'] = content
    return jsonify(result)
