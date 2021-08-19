def findW(v):
    for i in lst[v]:
        if visited[i] == False:
            return i
    return -1
def dfs(v):
    visited[v] = True
    ST.append(v)
    while len(ST) > 0:
        w = findW(v)
        if w != -1:
            ST.append(v)
            visited[w] = True
            v = w
        else:
            v = ST.pop(-1)
    return visited

import sys
sys.stdin = open('sample_input (2).txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        lst[v1].append(v2)
    start, end = map(int, input().split())

    visited = [False] * (V + 1)  # 0번 비워놓기
    ST = []  # 스택
    dfs(start)

    if visited[end]:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')