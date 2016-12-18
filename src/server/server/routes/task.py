from flask import request, jsonify

from server import app
from server.utils import json_abort
from server.models import *

myLists = [
    List('Inbox', id='0'),
    List('Groceries', id='1')
]
myTasks = [
    Task('Think about lunch', '1', id='0', status = Task.COMPLETED),
    Task('Become a pro in backend development', '0', id='1', status= Task.NORMAL),
    Task('CONQUER THE WORLD!', '0', id='2', status = Task.NORMAL)
]

# MARK: Task routes
@app.route('/api/lists/<string:list_id>/tasks', methods=['GET'])
def get_tasks(list_id):
    response = {}
    response['tasks'] = [t.__dict__ for t in myTasks if t.list==list_id]
    return jsonify(response)

# CREATE ROUTE
@app.route('/api/lists/<string:list_id>/tasks', methods=['POST'])
def create_task(list_id):
    ''' creates a new task for a list '''

    # 1. Check whether the specified list exists
    if (len([l for l in myLists if l.id == list_id]) < 1):
        json_abort(404, 'List not found')

    # 2. Check whether the required parameters have been sent
    try:
         data = request.get_json()
    except:
        json_abort(400, 'No JSON provided')

    if data == None:
        json_abort(400, 'Invalid Content-Type')

    title = data.get('title', None)
    if title == None:
        json_abort(400, 'Invalid request parameters')

    id = max([int(t.id) for t in myTasks]+[-1]) + 1
    newTask = Task(title, list_id, id=str(id), status = Task.NORMAL)

    # 4. append task to array
    myTasks.append(newTask)

    # 5. return new task
    return jsonify(newTask.__dict__)


@app.route('/api/lists/<string:list_id>/tasks/<string:task_id>', methods=['POST'])
def delete_task(list_id, task_id):
    if (len([l for l in myLists if l.id == list_id]) < 1):
        json_abort(404, 'List not found')
    tasks = [t for t in myTasks if t.id == task_id and t.list == list_id]
    if (len(tasks) < 1):
        json_abort(404, 'Task not found')
    myTasks.remove(tasks[0])
    return jsonify({'result': True})

@app.route('/api/lists/<string:list_id>/tasks/<string:task_id>', methods=['PUT'])
def update_task(list_id, task_id):
    if (len([l for l in myLists if l.id == list_id]) < 1):
        json_abort(404, 'List not found')
    if (len([t for t in myTasks if t.id == task_id]) < 1):
        json_abort(404, 'Task not found')
    try:
        data = request.get_json()
    except:
        json_abort(400, "You didn't give a json, dummy!")
    if data ==None:
        json_abort(400, "You did give a invalid content type, dummy!")

    title = data.get('title', None)
    status = data.get('status', None)
    description = data.get('description', None)
    due = data.get('due', None)
    revision = data.get('revision', None)
    updated_task = None
    if title == None or status == None or description == None or revision == None:
        json_abort(400, 'Invalid request parameters')
    for t in myTasks:
        if t.id == task_id and revision >= t.revision:
            t.title = title
            t.status = status
            t.description = description
            t.due = due
            t.revision += 1
            updated_task = t

    if updated_task == None:
        json_abort(404, 'Task not found, dummy')
    return jsonify(updated_task.__dict__)