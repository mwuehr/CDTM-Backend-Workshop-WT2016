from utils import *

def db_get_task_for_list(list_id):
    query = 'SELECT DISTINCT title FROM Tasks WHERE list = ? ORDER BY created DESC'

    db = get_db()
    cur = db.cursor()
    cur.execute(query, [list_id])
    Tasks = []
    for row in cur:
        Tasks.append(dict_from_row(row).get('type'))
    return Tasks

def db_get_task(task_id):
    query = 'SELECT DISTINCT title FROM Tasks WHERE id = ? ORDER BY created DESC'

    db = get_db()
    cur = db.cursor()
    cur.execute(query, [list_id])
    Tasks = []
    for row in cur:
        Tasks.append(dict_from_row(row).get('type'))
    return Tasks

def db_create_task(title, list):
    query = 'INSERT INTO Tasks SET (title, list, status) VALUES(?,?,?)'

    db = get_db()
    cur = db.cursor()
    cur.execute(query, [title, list, 'normal'])

def db_update_tasks(id, title, list, status, description, due):
    query = 'UPDATE Tasks (title, list, status, description, due, revision) VALUES (?,?,?) WHERE id = ?'

    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT revision FROM Tasks WHERE id = ?', [id])
    revision = int(cur[0]) + 1
    cur.execute(query, [title, list, status, description, due, revision])

def db_delete_tasks(id):
    query = 'DELETE FROM Tasks WHERE id = ?'

    db = get_db()
    cur = db.cursor()
    cur.execute(query, [id])