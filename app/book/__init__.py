# coding:utf8
from flask import Blueprint

book = Blueprint("book", __name__)

from app.book import views
