'''
DFS
각각 케이스별로 최대 거리 찾기
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, cnt, IsK):
    global ans
    if ans < cnt:
        ans = cnt
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if visited[nx][ny] == 1:
            continue
        if graph[x][y] > graph[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, IsK)
            visited[nx][ny] = 0
        elif graph[x][y] <= graph[nx][ny] and not IsK:
            for i in range(1, k+1):
                graph[nx][ny] -= i
                IsK = True
                if graph[x][y] > graph[nx][ny]:
                    visited[nx][ny] = 1
                    dfs(nx, ny, cnt+1, IsK)
                    visited[nx][ny] = 0
                IsK = False
                graph[nx][ny] += i

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    maxV = max(graph[0])
    for i in range(1, n):
        if maxV < max(graph[i]):
            maxV = max(graph[i])

    ans = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == maxV:
                visited = [[0]*n for _ in range(n)]
                visited[i][j] = 1
                dfs(i, j, 1, False)

    print(f'#{tc} {ans}')