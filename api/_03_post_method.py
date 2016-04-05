import json
from flask import Flask, Response, request
from .utils import JSON_MIME_TYPE

app = Flask(__name__)

LAST_ID = 33
books = [{
    'id': 33,
    'title': 'The Raven',
    'author_id': 1
}]


@app.route('/book')
def book_list():
    response = Response(
        json.dumps(books), status=200, mimetype=JSON_MIME_TYPE)
    return response


@app.route('/book', methods=['POST'])
def book_create():
    global LAST_ID
    assert request.content_type == JSON_MIME_TYPE

    LAST_ID += 1

    data = request.json
    books.append({
        'id': LAST_ID,
        'title': data['title'],
        'author_id': data['author_id']
    })

    response = Response(
        "", status=201, mimetype='application/json')
    return response
