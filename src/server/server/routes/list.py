from flask import jsonify

from src.server.server import app
from task import myLists


# MARK: List routes
@app.route('/api/lists', methods=['GET'])
def get_lists():
    response = {}
    response['lists'] = [l.__dict__ for l in myLists]
    return jsonify(response)
