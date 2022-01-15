from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break

    graph = [list(map(int, input().split())) for _ in range(b)]
    visited = [[0] * a for _ in range(b)]

    island_list = list()
    for i in range(b):
        for j in range(a):
            if graph[i][j] == 1:
                island_list.append((i, j))
    q = deque()
    cnt = 0
    for island in island_list:
        if visited[island[0]][island[1]]: continue
        q.append(island)
        cnt += 1
        while q:
            x, y = q.popleft()
            visited[x][y] = 1
            for d in range(8):
                nx = x + dx[d]
                ny = y + dy[d]
                if not 0 <= nx < b or not 0 <= ny < a: continue
                if not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    print(cnt)
