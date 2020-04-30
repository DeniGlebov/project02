from flask import Flask, request, Response
from utils import generate_password
from parsers import parse_length
from db import run_query, ordering, filter_and

app = Flask(__name__)


@app.route('/random/')
def hello_world():  # вью функция, эндпоинт

    # return redirect('https://pythonworld.ru/')
    length = parse_length(request.args.get('length', '10'))

    if type(length) is str:
        return Response(length, status=400)

    response = Response(generate_password(length) + '\n')

    return response


@app.route('/customers/')
def customers():
    query = '''
    SELECT * FROM customers
    '''

    country = request.args.get('country')
    if country:
        param = f" WHERE Country = '{country}'"
        query += param

    order = request.args.get('ordering')
    if order:
        param = f" ORDER BY {ordering(order)}"
        query += param

    param = request.args.get('filter')
    if param:
        query = f" SELECT * FROM customers WHERE {filter_and(param)}"

    query += ';'
    return str(run_query(query))


@app.route('/employees/')
def employees():
    query = '''
        SELECT * FROM employees;
    '''
    return str(run_query(query))


@app.route('/f/')
def foo():
    query = '''
        SELECT UnitPrice, Quantity FROM invoice_items;
    '''
    results = run_query(query)
    sum_ = 0
    for price, quantity in results:
        sum_ += price * quantity

    return str(sum_)


@app.route('/f2/')
def foo2():
    query = '''
        SELECT SUM(UnitPrice * Quantity) FROM invoice_items;
    '''
    return str(run_query(query))


@app.route('/names/')
def names():
    query = '''
        SELECT DISTINCT FirstName FROM customers;
    '''
    return str(run_query(query))


@app.route('/tracks/')
def tracks():
    query = '''
        SELECT COUNT(*) FROM tracks;
    '''
    return str(run_query(query))


@app.route('/tracks-sec//')
def tracks_sec():
    query = '''
        SELECT Name, (Milliseconds / 60) FROM tracks;
    '''
    return str(run_query(query))


if __name__ == '__main__':
    app.run(debug=True)
