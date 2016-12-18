from flask import jsonify

from server import app
from server.database import *


# MARK: List routes
@app.route('/api/lists', methods=['GET'])
def get_lists():
    return jsonify(db_get_lists())
