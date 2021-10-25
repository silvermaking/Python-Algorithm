"""
연결된 모든 지점을 재귀적으로 탐색하고 visited 처리
=> dfs
=> 재귀한도 초과 (파이썬의 재귀 한도가 1000으로 낮음) : sys.getrecursionlimit()
    - 배추의 개수가 최대 2500개 까지
=> 재귀한도 풀기
    - sys.setrecursionlimit(10000)

---------------------------------------------
graph[y][x]가 배추면(==1)
graph[y][x] = 0 (방문처리 해주고)
상하좌우를 재귀적으로 탐색
-> 연결된 모든 부분 방문처리

전체 graph를 탐색하며 dfs == True면
result += 1

"""
import sys
sys.setrecursionlimit(2510)

def dfs(y, x):
    if not 0 <= x < M or not 0 <= y < N:
        return

    if graph[y][x]:
        graph[y][x] = 0
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y, x-1)
        dfs(y, x+1)
        return True
    return False


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[y][x] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                result += 1

    print(result)