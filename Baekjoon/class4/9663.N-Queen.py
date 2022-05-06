"""
현재 백준 시간초과 현상
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[int(input())])
"""


import sys

def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i] - col[x]) == x - i:
            return False
    return True


def dfs(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        col[x] = i
        if check(x):
            dfs(x + 1)

N = int(sys.stdin.readline())
cnt = 0
col = [0] * 15
dfs(0)
print(cnt)