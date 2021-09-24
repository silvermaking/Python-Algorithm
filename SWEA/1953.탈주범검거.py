'''
BFS
'''
from collections import deque
tunnel = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}
def bfs(x, y, L):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in tunnel[graph[x][y]]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 이어진길인지 판별
            if (-dx, -dy) in tunnel[graph[nx][ny]]:
                #visited 중복 안되게
                if not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    if visited[nx][ny] <= L:
                        cnt += 1
    return cnt

for tc in range(1, int(input())+1):
    # 지도: (N, M), 맨홀: (R, C), L:소요시간
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    print(f'#{tc} {bfs(R, C, L)}')

