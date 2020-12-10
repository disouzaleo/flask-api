from flask import Flask

flask_app = Flask('flask-api')

@flask_app.route('/')
def index():
    return ''
