"""Handling Multiple Errors"""


def d_fn(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError) as err:
        print(f'Something went wrong! ({err})')
    # except ZeroDivisionError as err:
    #     print(f'Make sure that you don\'t divide by zero ({err})')


# result = d_fn(10, 5)
# result = d_fn(10, 'f')
result = d_fn(10, 0)
if result is not None:
    print(result)
