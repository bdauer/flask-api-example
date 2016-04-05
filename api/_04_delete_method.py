import json
from flask import Flask, Response, request, abort
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


@app.route('/book/<int:book_id>', methods=['DELETE'])
def book_delete(book_id):
    assert request.content_type == JSON_MIME_TYPE

    for idx, book in enumerate(books):
        if book['id'] == book_id:
            del books[idx]
            return "", 204, {'Content-Type': JSON_MIME_TYPE}

    abort(404)


@app.errorhandler(404)
def not_found(e):
    return '', 404
