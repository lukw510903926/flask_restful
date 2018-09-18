
from app.book import book


@book.route('/book/list')
def book_list():
    return 'book_list'
