'''
5209랑 비슷
확률 계산만 추가
소숫점 대소 비교(자릿수 맞춰주기)
파이썬의 반올림은 한계가 있다(이 문제는 상관 x)
'''
# import sys
# sys.stdin = open('input1865.txt', "r")
def dfs(staff):
    global answer, p
    if p <= answer: return

    if staff == N:
        answer = p
        return

    for i in range(N):
        if not visited[i] and graph[staff][i]:
            visited[i] = 1
            p *= graph[staff][i]/100
            dfs(staff + 1)
            visited[i] = 0
            p /= graph[staff][i]/100
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N #확률 체크
    p = 100
    answer = 0
    dfs(0)
    print(f'#{tc} {answer:.6f}')

