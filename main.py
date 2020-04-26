from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return ''


@app.route('/requirements/')
def requirements():
    return 'requirements'


@app.route('/generate-users/')
def generate_users():
    return 'generate-users'


@app.route('/mean/')
def mean():
    return 'mean'


@app.route('/space/')
def space():
    return 'space'


if __name__ == '__main__':
    app.run()
