from app.home import home
from flask import jsonify


@home.route('/dict')
def dict_map():
    maps = {'key': 'value', 'key2': 'value222222'}
    return jsonify(maps)
