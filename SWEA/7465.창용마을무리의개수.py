"""
5248 그룹나누기와 똑같은 문제
서로소 집합문제
"""

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for tc in range(1, int(input()) + 1):
    #N: 사람 수, M: 신청서
    N, M = map(int, input().split())
    lst = []
    for _ in range(M):
        a = list(map(int, input().split()))
        lst.extend(a)
    parent = [i for i in range(N+1)]
    for i in range(0, M*2, 2):
        a, b = lst[i], lst[i+1]
        union(a, b)
    team = set()
    for i in range(1, N+1):
        team.add(find(i))

    print(f'#{tc} {len(team)}')