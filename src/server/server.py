#!/usr/bin/env python
# coding: utf8

from flask import Flask, send_file, jsonify, request
import sys
import json
from list import List
from task import Task
from utils import json_abort

# allow special characters (e.g. üäö ...)
reload(sys)
sys.setdefaultencoding('utf-8')

# Note: Setting static_url_path to '' has the following effect:
#   - Whenever a file is requested and there is no matching route defined
#     the flask server will look whether the file is in the 'static/' folder
#   - As a consequence, everyone can remotely access files within 'static/'
#   - We need this, so that the front-end works properly.
app = Flask(__name__, static_url_path='')

api_version = '4.0'

lists = [List("CDTM Backend Workshop", id='0'), List("Social Entrepreneurship Workshop", id='1')]
tasks = [Task("Fabi crushen!!!", '0', status='completed'), Task("Mit Fabi fruehstuecken", '0'), Task("Bier kaufen", '1')]

lists[0].id

@app.route('/', methods=['GET'])
def root():
    return send_file('index.html')


@app.route('/api/version', methods=['GET'])
def version():
    return json.dumps({'version': api_version})


@app.route('/api/lists', methods=['GET'])
def return_lists():
    response = {}
    response['lists'] = [x.__dict__ for x in lists]
    return jsonify(response)


@app.route('/api/lists/<string:list_id>/tasks', methods=['GET'])
def return_tasks_in_list(list_id):
    response = {}
    response['tasks'] = [y.__dict__ for y in tasks if y.list == list_id]
    return jsonify(response)


@app.route('/api/lists/<string:list_id>/tasks', methods=['POST'])
def create_task(list_id):
    input_json = request.get_json(force=True)
    l = True
    if input != '':
        for x in lists:
            if list_id == x.id:
                tasks.append(Task(input_json.title, list_id))
                l = False
    if l:
        json_abort('404', "The list id doesn't exist")





if __name__ == '__main__':
    app.run(host='localhost', port=1337, debug=True)
