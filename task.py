# #!/usr/bin/python
# # -*- coding:utf-8 -*-
import json
import time

from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user

from ext import rd, db
from models import DBTask

bp = Blueprint('model', __name__, url_prefix='/task')


@bp.route('/run', methods=['POST'])
@login_required
def run():
    user = current_user.id
    if request.method == 'POST':
        now = time.localtime(time.time())
        data = request.get_data().decode()
        # print(data)
        data = json.loads(data)
        try:
            db_task = DBTask(
                user=user,
                subtime=now,
                status="Ready",
                task=json.dumps(data['data']),
                title=data['title'],
                note=data['note'],
            )
            db.session.add(db_task)
            db.session.commit()
            # row = DBTask.query.filter(DBTask.user == user, DBTask.subtime == now).first()
            task_id = str(db_task.id)
            rd.rpush('task', task_id)
            return jsonify({'status': 1})
        except:
            return jsonify({'status': -1})


@bp.route('/', methods=['GET'])
@login_required
def task():
    user = current_user.id
    rows = DBTask.query.filter(DBTask.user == user).all()
    result = {'size': len(rows)}
    content = []
    for row in rows:
        tmp = dict()
        tmp['submitTime'] = row.subtime
        tmp['endTime'] = row.endtime
        tmp['status'] = row.status
        tmp['task'] = json.loads(row.task)
        tmp['id'] = row.id
        tmp['title'] = row.title
        tmp['note'] = row.note
        content.append(tmp)
    result['content'] = content
    return jsonify(result)


@bp.route('/td/<task_id>', methods=['POST'])
@login_required
def td(task_id):
    try:
        res = DBTask.query.filter(DBTask.id == task_id).first()
        res.is_deleted = True
        db.session.commit()
        return jsonify({
            'status': 1,
            'message': 'success',
        })
    except Exception as e:
        print(e)
        return jsonify({
            'status': 0,
            'message': str(e),
        })
