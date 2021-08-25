#큐

for _ in range(1, 11):
    tc = int(input())
    password = list(map(int, input().split()))
    i = 1
    while True:
        a = password.pop(0) - i
        if a<0:
            a = 0
        password.append(a)
        if a<=0:
            break
        i += 1
        if i > 5: #5번이 한 사이클
            i = 1
    print('#{}'.format(tc), end=' ')
    print(*password)
