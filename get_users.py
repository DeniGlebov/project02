from faker import Faker


def user_generator(number):
    fake = Faker()
    text = ''
    for _ in range(number):
        text += (fake.name() + ' ' + fake.email() + ', ')
        text += '\n'

    return text
