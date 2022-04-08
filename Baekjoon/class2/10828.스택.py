import sys

input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x = input().split()
    order = x[0]
    if order == 'push':
        lst.append(x[1])
    elif order == 'top':
        if lst:
            print(lst[-1])
        else:
            print(-1)
    elif order == 'pop':
        if lst:
            print(lst.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(lst))

    elif order == 'empty':
        if lst:
            print(0)
        else:
            print(1)
