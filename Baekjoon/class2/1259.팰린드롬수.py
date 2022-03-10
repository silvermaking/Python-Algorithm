while True:
    n = input()
    if n == '0':
        break

    inverse_n = n[::-1]
    if n == inverse_n:
        print('yes')
    else:
        print('no')