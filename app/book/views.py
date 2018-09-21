import json

from app import app
from app.book import book
from app.model.system import Permission


@book.route('/book/list')
def book_list():
    permissions = Permission.query.all()
    app.logger.info(permissions)
    return json.dumps(Permission.to_list_dict(permissions), ensure_ascii=False)
