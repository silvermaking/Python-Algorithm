'''
완전탐색
순열 이용
'''
def perm(n, k):
    global minV
    if k == n:
        sumV = 0
        lst.insert(0, 0)
        lst.append(0)
        for i in range(1, len(lst)):
            sumV += e[lst[i-1]][lst[i]]
        if minV > sumV:
            minV = sumV
        lst.pop()
        lst.pop(0)
    else:
        for i in range(k, n):
            lst[k], lst[i] = lst[i], lst[k]
            perm(n, k+1)
            lst[k], lst[i] = lst[i], lst[k]

for tc in range(1, int(input()) + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    minV = 100 * N * 2
    lst = [i for i in range(1, N)]
    perm(N-1, 0)

    print(f'#{tc} {minV}')