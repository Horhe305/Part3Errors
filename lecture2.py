"""Error handling"""
x = 9
while True:
    try:
        user_num = int(input('Enter a number: '))
        print(user_num + x)
    except ValueError as val_err:
        print(f'Value Error! ({val_err})')

    else:
        break
