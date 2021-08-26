#BFS
#노드의 거리

def IsSafe(y, x):
    return 0 <= y < N and 0 <= x < N and (maze[y][x] == 0 or maze[y][x] == 3)
def bfs(y, x):
    q = []
    visited = [[0]* (N) for _ in range(N)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    q.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.pop(0)
        for dir in range(4):
            new_y = y + dy[dir]
            new_x = x + dx[dir]
            if IsSafe(new_y, new_x) and not visited[new_y][new_x]:
                q.append((new_y, new_x))
                visited[new_y][new_x] = 1
                distance[new_y][new_x] = distance[y][x] + 1
                if maze[new_y][new_x] == 3:
                    return distance[new_y][new_x] - 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                y, x = i, j
                break
    distance = [[0]* (N+1) for _ in range(N+1)]
    rse = bfs(y, x)
    print(f'#{tc} {rse}')