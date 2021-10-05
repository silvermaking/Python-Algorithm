'''
완전탐색
--------
트리모양
재귀로 풀기

'''
def solve(curX, curY, sumV):
    global minV
    if curX == N-1 and curY == N-1:
        if sumV < minV:
            minV = sumV
        return

    if curX < N-1:
        solve(curX+1, curY, sumV+graph[curX+1][curY])
    if curY < N-1:
        solve(curX, curY+1, sumV+graph[curX][curY+1])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    minV = 9 * (N * 2)
    solve(0, 0, graph[0][0])
    print(f'#{tc} {minV}')



