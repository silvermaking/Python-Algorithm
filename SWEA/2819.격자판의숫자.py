'''
완전탐색 dfs이용
backtraking
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x,y, word):
    if len(word) == 7:
        visited.add(word)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            continue
        dfs(nx, ny, word+graph[nx][ny])

for tc in range(1, int(input()) + 1):
    graph = [input().split() for _ in range(4)]
    n = len(graph)
    visited = set()
    for x in range(n):
        for y in range(n):
            dfs(x, y, graph[x][y])
    ans = len(visited)
    print("#{} {}".format(tc, ans))