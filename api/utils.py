JSON_MIME_TYPE = 'application/json'


def search_book(books, book_id):
    for book in books:
        if book['id'] == book_id:
            return book
