import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def virus(q):
    global max_ans
    tmp_graph = deepcopy(graph)
    cnt = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not 0 <= nx < N or not 0 <= ny < M: continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append((nx, ny))

    for i in range(N):
        cnt += tmp_graph[i].count(0)

    max_ans = max(max_ans, cnt)


def dfs(start, n):
    if n == 0:
        q = deepcopy(v_queue)
        virus(q)
        return

    for i in range(start, N*M):
        r = i // M
        c = i % M
        if graph[r][c]: continue
        graph[r][c] = 1
        dfs(i, n-1)
        graph[r][c] = 0


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
max_ans = 0
v_queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            v_queue.append((i, j))

dfs(0, 3)
print(max_ans)