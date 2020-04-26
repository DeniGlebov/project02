def requirements_state():
    with open('requirements.txt') as file:
        req = file.read()
    return req