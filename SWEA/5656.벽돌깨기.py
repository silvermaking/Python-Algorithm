'''
if 문 쓸 때 0가 boolean 같이 쓰지 말기 -> 헷갈림
find()함수에서 i가 0일 경우 if find(): 하면 false이므로
dfs

'''
import copy
def find(x, lst):  # 숫자만 사용
    for i in range(H):
        if lst[i][x]:
            return i
    return -1
def impact(x, y, lst):
    if lst[x][y] == 0:
        return
    a = lst[x][y]
    lst[x][y] = 0
    for i in range(1, a):
        if 0 <= (x-i):
            impact(x-i, y, lst)
        if (x+i) < H:
            impact(x+i, y, lst)
        if 0 <= (y-i):
            impact(x, y-i, lst)
        if (y+i) < W:
            impact(x, y+i, lst)
def restore(lst, lst2):
    for j in range(W):
        temp = []
        for i in range(H):
            if lst[i][j]:
                temp.append(lst[i][j])
        for k in range(len(temp)):
            lst2[H-len(temp)+k][j] = temp[k]

def solve(k, graph):
    global ans
    # 벽돌 N개 쓰기전에 다 부실경우
    i = 0
    while True:
        if i == W:
            ans = 0
            return
        if find(i, graph): break
        i += 1

    if k == N:
        cnt = 0
        for i in range(H):
            cnt += graph[i].count(0)
        result = W*H - cnt
        if result < ans:
            ans = result
        return

    for i in range(W):
        if find(i, graph) >= 0:
            x = find(i, graph)
            graph2 = copy.deepcopy(graph)
            #부시기
            impact(x, i, graph2)
            #벽돌 정리
            graph3 = [[0 for _ in range(W)] for _ in range(H)]
            restore(graph2, graph3)
            solve(k+1, graph3)

T = int(input())
for tc in range(1, T + 1):
    # N : 한 변의 길이
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]
    ans = 180
    solve(0, graph)
    print(f'#{tc} {ans}')
