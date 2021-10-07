'''
순열로 풀어보기

'''
def solve(k, cost):
    global minV
    if minV <= cost:
        return
    if k == N:
        if minV > cost:
            minV = cost
        return

    for i in range(N):
        if not visited[i]:
            res[k] = i
            visited[i] = 1
            solve(k+1, cost + graph[k][i])
            visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    res = [-1] * N
    minV = 100 * N
    solve(0, 0)
    print(f'#{tc} {minV}')