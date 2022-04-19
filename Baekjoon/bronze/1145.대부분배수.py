lst = list(map(int, input().split()))
a = min(lst)
while True:
    x = a
    cnt = 0
    for j in lst:
        if x % j == 0:
            cnt += 1

    if cnt > 2:
        print(x)
        break

    a += 1