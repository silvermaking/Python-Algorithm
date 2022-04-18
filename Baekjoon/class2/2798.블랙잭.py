import sys


def solve(s, cnt):
    global max_ans
    if s > M:
        return
    if cnt == 3:
        max_ans = max(s, max_ans)
        return

    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        solve(s+lst[i], cnt+1)
        visited[i] = 0


input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
visited = [0] * (N + 1)
max_ans = 0
solve(0, 0)
print(max_ans)