# pip install requests
# pip install flask

import requests
from flask import Flask, request

app = Flask(__name__)


TARGET_URL = ""


@app.route('/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def hello_world():
    get_args = request.args
    post_data = request.form
    request_method = request
    response = requests.request(request_method, TARGET_URL, data=post_data,
                                headers=request.headers)
    return response.content, response.status_code

