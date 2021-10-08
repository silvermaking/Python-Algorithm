'''
완전탐색 + backtracking
bfs 는 중복이 많아 비효율적
bfs 와 비슷하게 visited를 idx기준으로

'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N ** 2)
    for x in range(N):
        for y in range(N):
            idx = graph[x][y]
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not 0 <= nx < N or not 0 <= ny < N:
                    continue
                if graph[nx][ny] == (idx + 1):
                    visited[idx] = 1
                    break
    max_cnt = 0
    i = 0
    while i < len(visited):
        if visited[i] == 1:
            temp = i
            cnt = 2
            while i< len(visited) - 1:
                i += 1
                if visited[i] == 1:
                    cnt += 1
                else:
                    i -= 1
                    break
            if cnt > max_cnt:
                ans_idx = temp
                max_cnt = cnt
        i += 1
    print(f'#{tc} {ans_idx} {max_cnt}')