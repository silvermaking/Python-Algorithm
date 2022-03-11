while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break

    lst = [a, b, c]
    lst.sort()
    a, b, c = lst[0], lst[1], lst[2]

    if a ** 2 + b ** 2 == c ** 2:
        print('right')
    else:
        print('wrong')