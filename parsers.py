def parse_length(length: str) -> int or str:
    if not length.isdigit():
        return f'Incorrect parameter length: {length}'

    length = int(length)

    if length > 100 or length < 5:
        return f'Incorrect length value: {length}. must be in range [5, 100]'

    return length
