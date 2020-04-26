from get_requirements import requirements_state
from get_users import user_generator
from utils import parse_number, middle, parse_space
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def start():
    return ''


@app.route('/requirements/')
def requirements():
    return requirements_state()


@app.route('/generate-users/')
def generate_users():
    number = parse_number(request.args.get('number', '1'))

    if type(number) is str:
        return Response(number, status=400)

    return user_generator(number)


@app.route('/mean/')
def mean():
    with open('hw.csv') as file:
        data = file.read()
        data = data.split('\n')
        data = data[1:-2]
    return middle(data)


@app.route('/space/')
def space():
    return parse_space()


if __name__ == '__main__':
    app.run()