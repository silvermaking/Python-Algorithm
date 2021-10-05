'''
교수님 풀이
'''
def perm(k):
    global minV
    if k == N:
        res[-1] = 0
        # print(res)
        sumV = 0
        for i in range(N):
            start = res[i]
            end = res[i+1]
            sumV += e[start][end]
        if minV > sumV:
            minV = sumV
        return

    for i in range(N):
        if not visited[i]:
            res[k] = i
            visited[i] = True
            perm(k+1)
            visited[i] = False

for tc in range(1, int(input()) + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    res = [-1] * (N+1)
    res[0] = 0
    visited = [False] * N
    visited[0] = True
    minV = 123456789
    perm(1)
    print(f'#{tc} {minV}')