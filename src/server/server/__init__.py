#!/usr/bin/env python
# coding: utf8

import sys

from flask import Flask, send_file, request, jsonify

# allow special characters (e.g. üäö ...)
reload(sys)
sys.setdefaultencoding('utf-8')

# init app before importing models
app = Flask(__name__, static_url_path='')

from models import *
from routes import *
from utils import json_abort


# Note: Setting static_url_path to '' has the following effect:
#   - Whenever a file is requested and there is no matching route defined
#     the flask server will look whether the file is in the 'static/' folder
#   - As a consequence, everyone can remotely access files within 'static/'
#   - We need this, so that the front-end works properly.