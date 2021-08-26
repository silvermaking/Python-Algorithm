# BFS ,DFS
def bfs(y, x):
    q = []
    visited = [[0] * 16 for _ in range(16)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    q.append((y, x))
    visited[y][x] = 1
    if lst2[y][x] == 3:
        return 1
    while q:
        y, x = q.pop(0)
        for dir in range(4):
            new_y = y + dy[dir]
            new_x = x + dx[dir]
            if lst2[new_y][new_x] == 3:
                return 1
            if lst2[new_y][new_x] == 0 and not visited[new_y][new_x]:
                q.append((new_y, new_x))
                visited[new_y][new_x] += 1
    return 0

for test_case in range(1, 11):
    tc = int(input())
    lst2 = [list(map(int, input())) for _ in range(16)]
    y, x = 1, 1
    print(f'#{tc} {bfs(y, x)}')
