import copy
def drop(pos, graph):
    ST = []
    row = 0
    while row<H and graph[row][pos] == 0:
        row += 1
    if row == H:
        return
    ST.append((pos, row))
    while ST:
        curX, curY = ST.pop()
        size = graph[curY][curX]
        graph[curY][curX] = 0
        for i in range(size):
            if curY - i >=0 and graph[curY-i][curX]:
                ST.append((curX, curY-i))
            if curY + i < H and graph[curY+i][curX]:
                ST.append((curX, curY+i))
            if curX - i >= 0 and graph[curY][curX-i]:
                ST.append((curX-i, curY))
            if curX + i < W and graph[curY][curX+i]:
                ST.append((curX+i, curY))
def clean(graph):
    for x in range(W):
        desP = srcP = H-1
        while srcP >= 0:
            if graph[srcP][x]:
                graph[desP][x] = graph[srcP][x]
                desP -= 1
            srcP -= 1
        while desP >= 0:
            graph[desP][x] = 0
            desP -= 1

def solve(k, graph):
    global ans
    if k == N:
        cnt = 0
        for i in range(H):
            cnt += graph[i].count(0)
        result = W*H - cnt
        if result < ans:
            ans = result
        return
    for i in range(W):
        temp = copy.deepcopy(graph)
        res[k] = i
        drop(i, graph)
        clean(graph)
        solve(k+1, graph)
        graph = copy.deepcopy(temp)

T = int(input())
for tc in range(1, T + 1):
    # N : 한 변의 길이
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]
    res = [-1] * N
    ans = 180
    solve(0, graph)
    print(f'#{tc} {ans}')