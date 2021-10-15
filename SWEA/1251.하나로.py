"""
그래프: 신장트리 문제
prim()
===============
- 숫자가 크므로 평소의 987654321로 안됨
float('inf') 이용
- 문자열 소수점 반환
{:.0f}
"""
# import sys
# sys.stdin = open('input1251t.txt', "r")
def weight(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) * E

def prim():
    s = 1
    D[s] = 0

    while len(U) <= N:
        #D의 key값이 최소인 정점을 구한다.
        #이 정점은 U에 포함되지 않아야 한다.
        minV = INF
        for i in range(N+1):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                curV = i
        # U에 추가
        U.append(curV)

        #curV의 인접한 정점의 가중치를 사용하여 D 업데이트
        for i in range(N+1):
            if i in U: continue
            if graph[curV][i]:
                if D[i] > graph[curV][i]:
                    D[i] = graph[curV][i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X_lst = list(map(int, input().split()))
    Y_lst = list(map(int, input().split()))
    E = float(input())
    graph = [[0] * (N+1) for _ in range(N+1)]
    for i in range(0, N):
        for j in range(i, N):
            w = weight(X_lst[i], Y_lst[i], X_lst[j], Y_lst[j])
            graph[i+1][j+1] = w
            graph[j+1][i+1] = w
    INF = float('inf')
    D = [INF] * (N+1)#0: key, 1: pi
    D[0] = 0
    U = []
    prim()
    print('#{} {:.0f}'.format(tc, sum(D)))