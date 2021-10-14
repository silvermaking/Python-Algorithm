"""
다익스트라 알고리즘
"""
def dijk():
    s = 0
    D[s][0] = 0

    for i in range(N+1):
        if graph[s][i]:
            D[i][0] = graph[s][i]

    while len(U) <= N:
        #D의 key값이 최소인 정점을 구한다.
        #이 정점은 U에 포함되지 않아야 한다.
        minV = 100000000
        for i in range(N+1):
            if i in U: continue
            if D[i][0] < minV:
                minV = D[i][0]
                curV = i
        # U에 추가
        U.append(curV)

    # curV의 인접한 정점의 가중치를 사용하여 D 업데이트
        for i in range(N + 1):
            if i in U: continue
            if graph[curV][i]:
                if D[i][0] > D[curV][0] + graph[curV][i]:
                    D[i][0] = D[curV][0] + graph[curV][i]
                    D[i][1] = curV
for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    graph = [[0] * (N+1) for _ in range(N+1)]
    for i in range(E):
        s1, s2, w = map(int, input().split())
        graph[s1][s2] = w

    D = [[100000000, 0] for _ in range(N+1)] #0: key, 1: pi
    U = []
    dijk()
    ans = 0
    print(f'#{tc} {D[N][0]}')