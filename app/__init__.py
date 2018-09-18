from flask import Flask
app = Flask(__name__)
# session 加密秘钥
app.config["SECRET_KEY"] = 'af2fad8cfe1f4c5fac4aa5edf6fcc8f3'
