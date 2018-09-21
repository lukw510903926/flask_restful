from app import app
from app.admin import admin
from app.home import home
from app.login import login_filter


# 拦截认证
@app.before_request
def my_redirect():
    login_filter.login_filter()
    app.logger.info('这是第一个warning log')


app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(home, url_prefix='/home')

if __name__ == '__main__':
    app.run(debug=True)
