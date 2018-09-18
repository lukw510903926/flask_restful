import json
from app import app
from app.admin import admin


@admin.route('/list')
def user_list():
    ls = (['physics', 'chemistry', 1997, 2000])
    ls.append('aa')
    app.logger.info('这是第一个warning log')
    return json.dumps(ls)
