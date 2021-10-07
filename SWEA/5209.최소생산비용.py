'''
생산비용 최소화
backtracking

'''
def dfs(product):
    global answer, cost
    if cost > answer: return

    if product == N:
        answer = cost
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            cost += graph[product][i]
            dfs(product + 1)
            visited[i] = 0
            cost -= graph[product][i]

for tc in range(1, int(input()) + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N #공장 체크
    cost = 0
    answer = 987654321
    dfs(0)

    print(f'#{tc} {answer}')