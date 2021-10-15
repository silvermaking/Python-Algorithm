"""
N: 정점, M: 간선, X: 목적지
========================
max 거리 구하기

"""
# import sys
# sys.stdin = open('input1795.txt', "r")
def dijstra(X, D, U, graph):
    s = X
    D[s] = 0

    while len(U) <= N:
        #D의 key값이 최소인 정점을 구한다.
        #이 정점은 U에 포함되지 않아야 한다.
        minV = 987654321
        for i in range(1, N+1):
            if i in U: continue
            if D[i]< minV:
                minV = D[i]
                curV = i
        # U에 추가
        U.append(curV)

        # curV의 인접한 정점의 가중치를 사용하여 D 업데이트
        for i in range(1, N + 1):
            if i in U: continue
            if graph[curV][i]:
                if D[i] > D[curV] + graph[curV][i]:
                    D[i] = D[curV] + graph[curV][i]
T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    adj1 = [[987654321] * (N+1) for _ in range(N+1)]
    adj2 = [[987654321] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c
    D1 = [987654321] * (N+1)
    D2 = [987654321] * (N+1)
    U1, U2 = [], []
    max_ans = 0
    dijstra(X, D1, U1, adj1)
    dijstra(X, D2, U2, adj2)
    for i in range(1, N+1):
        if D1[i] + D2[i] > max_ans:
            max_ans = D1[i] + D2[i]

    print(f"#{tc} {max_ans}")

