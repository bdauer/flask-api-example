import json
from flask import Flask, make_response

app = Flask(__name__)

data = {
    'id': 33,
    'title': 'The Raven',
    'author_id': 1
}


@app.route('/')
def book_list():
    content = json.dumps(data)
    response = make_response(
        content, 200, {'Content-Type': 'application/json'})
    return response
