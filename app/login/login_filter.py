from flask import request, session
from app.util.config import Logger
import json


def login_filter():
    logger = Logger(name='login_filter')
    session['name'] = 'www.zongk.com'
    # logger.info('session:' + session)
    logger.info('cookies:' + json.dumps(request.cookies))
    logger.log('sessionName : ' + session.get('name'))
