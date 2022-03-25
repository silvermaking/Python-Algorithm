import sys

input = sys.stdin.readline

C = int(input())
for _ in range(C):
    lst = list(map(int, input().split()))
    m = sum(lst[1:]) / lst[0]
    ans = 0
    for i in lst[1:]:
        if i > m:
            ans += 1

    res = (ans / lst[0]) * 100

    print(f'{res:.3f}%')