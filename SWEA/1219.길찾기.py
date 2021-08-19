def findW(v):
    for i in range(0, len(lst), 2):
        if v == lst[i] and visited[lst[i+1]]==False:
            return lst[i+1]

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
sys.stdin = open('input.txt', 'r')
for test_case in range(1, 11):
    TC, N = map(int, input().split())
    lst = list(map(int, input().split()))
    visited = [False] * 100
    ST = []  # 스택
    visited = dfs(0)
    if visited[-1]:
        print(f'#{TC} {1}')
    else:
        print(f'#{TC} {0}')