import sqlite3


def run_query(query: str) -> list:
    try:
        conn = sqlite3.connect('./chinook.db')
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        conn.close()
        return results
    except Exception:
        return None
    finally:
        conn.close()


def ordering(query_param: str) -> str:
    """
    country,-city
    """
    result = []
    for elem in query_param.split(','):

        if '-' in elem:
            result.append(f'{elem[1:].capitalize()} DESC')
        else:
            result.append(elem.capitalize())

    return ', '.join(result)


def filter_and(query_param: str) -> str:
    result = []
    if 'city' in query_param:
        query_param = query_param.replace('country', 'Country').replace('city', 'City')
        temp = query_param.split(';')
        s1 = (temp[0].replace(":", " = '"))
        s2 = (temp[1].replace(":", " = '"))

        result.append(f"{s1}' AND {s2}'")
    else:
        query_param = query_param.replace('country', 'Country')
        temp = query_param.split(':')
        result.append(f"{temp[0]} = '{temp[1]}'")

    return ' AND '.join(result)


if __name__ == '__main__':
    assert ordering('country,-city') == 'Country, City DESC'
    assert ordering('-country,-city') == 'Country DESC, City DESC'
    assert ordering('') == ''

    assert filter_and('country:USA;city:Boston') == "Country = 'USA' AND City = 'Boston'"
    assert filter_and('country:USA') == "Country = 'USA'"
