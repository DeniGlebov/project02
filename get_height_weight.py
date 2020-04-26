def height_weight(data):
    with open('hw.csv') as file:
        data = file.read()
        data = data.split('\n')
        data = data[1:-2]

    return data