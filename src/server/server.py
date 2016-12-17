#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file, jsonify
import sys
import json
from list import List
from task import Task

# allow special characters (e.g. üäö ...)
reload(sys)
sys.setdefaultencoding('utf-8')

# Note: Setting static_url_path to '' has the following effect:
#   - Whenever a file is requested and there is no matching route defined
#     the flask server will look whether the file is in the 'static/' folder
#   - As a consequence, everyone can remotely access files within 'static/'
#   - We need this, so that the front-end works properly.
app = Flask(__name__, static_url_path='')

api_version = '2.0'

lists = [List("CDTM Backend Workshop", id='0')]
tasks = [Task("Fabi crushen!!!", 0, status='completed'), Task("Mit Fabi frühstücken", 0)]

lists[0].id

@app.route('/', methods=['GET'])
def root():
    return send_file('index.html')


@app.route('/api/version', methods=['GET'])
def version():
    return json.dumps({'version': api_version})


@app.route('/api/lists', methods=['GET'])
def return_lists():
    return jsonify({'lists': lists[0].__dict__})


@app.route('/api/lists/<int:list_id>/task')
def return_tasks_in_list(list_id):
    selected_tasks = []
    output = []
    for i in tasks:
        if i.list == list_id:
            selected_tasks.append(i)
    for j in selected_tasks:
        output.append(j.__dict__)
    return jsonify({'tasks': output})


if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)
