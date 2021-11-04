"""
bfs : 치즈 제거
params: {
    cnt(int): 치즈 갯수
    time(int): 걸린 시간

}
==================
치즈일 때는 녹이기만 하고(겉면만), q에 추가 x
치즈가 아닐 때는 q.append()
"""

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(y, x):
    visited = [[0] * W for _ in range(H)]
    global cnt
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0 <= nx < W or not 0 <= ny < H: continue
            if not visited[ny][nx]:
                visited[ny][nx] = 1
                if graph[ny][nx]: # 치즈면 녹이고
                    graph[ny][nx] = 0
                    cnt -= 1
                else: # 아니면 queue에 추가
                    q.append((ny, nx))


H, W = map(int, input().split())
graph = [list(map(int, input().strip().split())) for _ in range(H)]
cnt = 0
time = 0
for lst in graph:
    cnt += lst.count(1)

while cnt:
    ans = cnt
    bfs(0, 0)
    time += 1

print(time, ans, sep='\n')