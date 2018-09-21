from flask import Flask
from logging.config import dictConfig
from app.util.file_util import make_dir
import os
import time
from flask_sqlalchemy import SQLAlchemy


log_dir_name = "logs"
log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + log_dir_name
make_dir(log_file_folder)
log_file_location = log_file_folder + os.sep + log_file_name


app = Flask(__name__)
# 数据库配置
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# session 加密秘钥
app.config["SECRET_KEY"] = 'af2fad8cfe1f4c5fac4aa5edf6fcc8f3'

# 放在数据库配置后执行
db = SQLAlchemy(app)
# 日志配置
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
