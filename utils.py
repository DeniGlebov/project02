import random
import string


def generate_password(length: int = 10) -> str:
    choices = string.ascii_letters + string.digits + string.punctuation

    password = ''
    for _ in range(length):
        password += random.choice(choices)

    return password


def parse_number(number):
    if not number.isdigit():
        return f'Incorrect parameter number user'

    number = int(number)

    if number > 300 or number < 1:
        return f'Incorrect number user,must be in range [2, 300]'

    return number


def middle(data):
    Height = {}
    key_Height = 0
    Weight = {}
    key_Weight = 0

    for value_Height in data:
        temp = float(value_Height.split(', ')[1])

        if temp not in Height:
            key_Height += 1
            Height[key_Height] = temp

    for value_Weight in data:
        temp = float(value_Weight.split(', ')[2])

        if temp not in Weight:
            key_Weight += 1
            Weight[key_Weight] = temp

    var_Height = [(value, key) for key, value in Height.items()]
    MaxHeight = max(var_Height)[0] * 2.54  # Считаем рост в СМ
    MinHeight = min(var_Height)[0] * 2.54  # Считаем рост в СМ
    middle_var_Height = (int(((MaxHeight + MinHeight) / 2) * 100)) / 100  # Средний рост

    var_Weight = [(value, key) for key, value in Weight.items()]
    MaxWeight = max(var_Weight)[0] * 0.453592  # Считаем вес в КГ
    MinWeight = min(var_Weight)[0] * 0.453592  # Считаем вес в КГ
    middle_var_Weight = (int(((MaxWeight + MinWeight) / 2) * 100)) / 100  # Средний вес

    return f'Средний рост: {middle_var_Height} см, Средний вес {middle_var_Weight} кг'


def parse_space():
    import requests

    r = requests.get('http://api.open-notify.org/astros.json')

    if '200' in str(r):
        data = str(r.text)
        data = data[(data.index('[')) + 1:(data.rindex(']'))]
        data = data.replace('{', '').replace('}', '').replace('"', '').replace(' ', '')
        data = data.split(',')
        temp_list = list()
        for i in data:
            if 'name:' in i:
                temp_list.append(i[5:])
        data = ' '.join(map(str, temp_list))

    return data
