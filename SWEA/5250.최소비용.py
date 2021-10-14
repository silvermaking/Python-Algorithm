"""
bfs
거리 구하는 아이디어

"""
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0 <= nx < N or not 0 <= ny < N:
                continue
            temp = 1
            if maps[ny][nx] > maps[y][x]:
                temp += maps[ny][nx] - maps[y][x]
            if distance[ny][nx] > distance[y][x] + temp:
                distance[ny][nx] = distance[y][x] + temp
                queue.append((ny, nx))

for tc in range(1, int(input()) + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = 0
    bfs(0, 0)
    print(f'#{tc} {distance[N-1][N-1]}')