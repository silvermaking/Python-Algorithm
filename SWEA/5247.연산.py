"""
bfs
backtraking : 한번 나온 숫자는 visited에 담아놈
"""
from collections import deque
def bfs(N):
    q = deque()
    q.append((N, 0))
    visited = [0] * 1000001
    while q:
        N, cnt = q.popleft()
        if visited[N]: continue
        visited[N] = 1
        if N == M:
            return cnt
            break
        if 1 <= N + 1 <= 1000000:
            q.append((N + 1, cnt+1))
        if 1 <= N - 1 <= 1000000:
            q.append((N - 1, cnt+1))
        if 1 <= N * 2 <= 1000000:
            q.append((N * 2, cnt+1))
        if 1 <= N - 10 <= 1000000:
            q.append((N - 10, cnt+1))

for tc in range(1, int(input()) + 1):
    # N: 시작 숫자, M: 만들 숫자
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N)}')