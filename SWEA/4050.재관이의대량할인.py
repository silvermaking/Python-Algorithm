"""
math

"""

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = sorted(list(map(int, input().split())), reverse=True)
    ans = sum(lst)
    for i in range(2, N, 3):
        ans -= lst[i]

    print(f'#{tc} {ans}')
