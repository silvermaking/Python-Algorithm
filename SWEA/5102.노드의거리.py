def bfs_adj(v):
    global answer
    q = []
    visited = [False] * (V+1)
    q.append(v)
    visited[v] = True
    while q: # 연결이 안되있으면 while문 탈출
        v = q.pop(0)
        for w in range(len(adj[v])):
            if adj[v][w] == 1 and not visited[w]:
                q.append(w) # 큐에 넣는다.
                visited[w] = True
                distance[w] = distance[v]+1
                if w == G:
                    answer = distance[w]
                    return


import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = []
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        v1, v2 =map(int, input().split())
        adj[v1][v2] = 1
        adj[v2][v1] = 1
    S, G = map(int, input().split())
    distance = [0] * (V+1)
    answer = 0
    bfs_adj(S)

    print('#{} {}'.format(tc, answer))