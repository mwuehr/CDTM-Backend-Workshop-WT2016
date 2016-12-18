from flask import request, jsonify

from server import app
from server.utils import *
from server.models import *
from server.database import *


# MARK: Task routes
@app.route('/api/lists/<string:list_id>/tasks', methods=['GET'])
@lists_exists
def get_tasks(list_id):
    return jsonify(db_get_tasks_for_list(list_id))

# CREATE ROUTE
@app.route('/api/lists/<string:list_id>/tasks', methods=['POST'])
@lists_exists
@has_json
def create_task(list_id):
    ''' creates a new task for a list '''

    data = request.get_json()
    title = data.get('title', None)
    if title == None:
        json_abort(400, 'Invalid request parameters')

    return jsonify(db_create_task(data.get('title'), data.get('list')))

    # 5. return new task


# DESTROY ROUTE
@app.route('/api/lists/<string:list_id>/tasks/<string:task_id>', methods=['DELETE'])
@lists_exists
@has_json
def remove_task(list_id, task_id):

    # 2. Check whether the specified task exists
    if (db_get_task(task_id) != ''):
        json_abort(404, 'Task not found')

    # 3. finally remove the task
    db_delete_task(task_id)
    return jsonify({'result': True})

# UPDATE ROUTE
@app.route('/api/lists/<string:list_id>/tasks/<string:task_id>', methods=['PUT'])
@lists_exists
@has_json
def update_task(list_id, task_id):
    # 2. Check whether the specified task exists
    if (db_get_tasks(task_id) != ''):
        json_abort(404, 'Task not found')

    # 3. Check whether the required parameters have been sent
    data = request.get_json()

    if data == None:
        json_abort(400, 'Invalid Content-Type')

    title = data.get('title', None)
    status = data.get('status', None)
    description = data.get('description', None)
    due = data.get('due', None)

    return jsonify(db_update_task (task_id, title, status, description, due))

