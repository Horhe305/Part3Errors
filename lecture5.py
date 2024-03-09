"""Raise an Error"""


def d_fn(a, b):
    try:
        if b == 1:
            raise Exception('Dividing by 1 is pointless')
        return a / b
    except (TypeError, ZeroDivisionError, Exception) as err:
        print(f'Something went wrong! ({err})')
    finally:
        return 'This block will run even with error above'


result = d_fn(10, 1)
print(result)
