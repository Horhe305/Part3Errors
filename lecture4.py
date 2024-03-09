"""Handling Errors - Finally Block"""


def d_fn(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError) as err:
        print(f'Something went wrong! ({err})')
    finally:
        return 'No matter what, this block will run'


result = d_fn(10, '2')
print(result)
