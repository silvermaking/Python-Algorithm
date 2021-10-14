"""
dfs로 풀어보기
서로소 집합 문제
"""
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[v]:
            dfs(i)

for tc in range(1, int(input()) + 1):
    #N: 사람 수, M: 신청서
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    for i in range(0, M*2, 2):
        a, b = lst[i], lst[i+1]
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(f'#{tc} {cnt}')

    # print(f'#{tc} {ans}')