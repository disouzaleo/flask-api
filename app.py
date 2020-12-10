from flask import abort, Flask

flask_app = Flask('flask-api')

@flask_app.route('/')
def index():
    return ''

@flask_app.route('/error')
def get_one_error():
    abort(404, description="Resource not found")


if __name__ == '__main__':
    flask_app.run()
