from collections import deque
def DFS(v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in G[v]:
        if not visited[i]:
            DFS(i, visited)

def BFS(v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in G[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, N+1):
    G[i].sort()

DFS(V, visited1)
print()
BFS(V, visited2)