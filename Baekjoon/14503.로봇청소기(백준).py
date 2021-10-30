"""
구현, 그래프 탐색
--------------------------
0 1 2 3
0 3 2 1
"""
# 북쪽 : -1 0 (0 1) (10) (0 -1)
# 동쪽 : (0, -1), (-1, 0)

import sys
input = sys.stdin.readline
# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(y, x, d):
    global cnt
    if graph[y][x] == 0:
        graph[y][x] = 2
        cnt += 1
    for _ in range(4):
        nd = (d + 3) % 4  # 0(북쪽 시작) : idx => 3 , 2, 1, 0 순
        nx = x + dx[nd]
        ny = y + dy[nd]
        if graph[ny][nx] == 0:
            dfs(ny, nx, nd)
            return
        d = nd
    nd = (d + 2) % 4 # 0(북쪽 시작) : idx => 2(반대방향)
    nx = x + dx[nd]
    ny = y + dy[nd]
    if graph[ny][nx] == 1:
        return
    dfs(ny, nx, d)

N, M = map(int, input().strip().split())
y, x, d = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]

cnt = 0
dfs(y, x, d)
print(cnt)