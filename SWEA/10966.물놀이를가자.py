'''
최소길찾기
BFS
- input을 리스트로 받으면 시간초과
    - 원래 아슬아슬해서 리스트로 바꾸는 함수만큼 시간초과
- input을 문자열로 받아야함
- 시간초과나면
    - backtracking
    - a not in list: 리스트에 있는거 다 체크
###########################################
땅에서 부터 하는 거 구현
선형큐 이용 front rear
'''
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    # pool = [list(input()) for _ in range(N)]
    pool = [input() for _ in range(N)]
    visited = [[987654321] * M for _ in range(N)]

    Q = deque()
    for i in range(N):
        for j in range(M):
            if pool[i][j] == 'W':
                Q.append((i, j))
                visited[i][j] = 0
    while Q:
        x, y = Q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # if not 0 <= nx < N or not 0 <= ny < M: continue
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] != 987654321:
                continue
            if pool[nx][ny] == 'L' and visited[nx][ny] == 987654321:
                visited[nx][ny] = visited[x][y] + 1
                Q.append((nx, ny))

    ans = 0
    for i in visited:
        for j in i:
            ans += j

    print('#{} {}'.format(tc, ans))