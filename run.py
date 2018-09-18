from app import app
from app.admin import admin
from app.home import home
from app.login import login_filter
from logging.config import dictConfig
from app.util.file_util import make_dir
import os
import time

log_dir_name = "logs"
log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + log_dir_name
make_dir(log_file_folder)
log_file_location = log_file_folder + os.sep + log_file_name

dictConfig({
    'version': 1,
    'formatters': {'default': {
        # 'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        'format': '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'level': 'INFO',
        'formatter': 'default'
    }, 'fileHandler': {
        'class': 'logging.FileHandler',
        'filename': log_file_location,
        'encoding': 'utf-8',
        'level': 'INFO',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'fileHandler']
    }
})


# 拦截认证


@app.before_request
def my_redirect():
    login_filter.login_filter()
    app.logger.info('这是第一个warning log')


app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(home, url_prefix='/home')

if __name__ == '__main__':
    app.run(debug=True)
