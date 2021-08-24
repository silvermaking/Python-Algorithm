import sys
sys.stdin = open('sample_input.txt', 'r')

def IsSafe(y, x):
    return 0 <= y < N and 0 <= x < N and (lst2[y][x] == 0 or lst2[y][x] == 3)

def DFS(y, x):
    global answer

    if lst2[y][x] == 3:
        answer = 1
        return
    visited.append((y, x))
    for dir in range(4):
        new_y = y + dy[dir]
        new_x = x + dx[dir]
        if IsSafe(new_y, new_x) and (new_y, new_x) not in visited:
            DFS(new_y, new_x)
# 교수님 풀이
# def dfs(curX, curY):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     ST = []
#     ST.append((curX, curY))
#     ARR[curY][curX] = 1 #방문했음
#     while ST:
#         (curX, curY) = ST.pop()
#         for d in range(4):
#             newX = curX + dx[d]
#             newY = curY + dy[d]
#             if 0<= newY < N  and 0<= newX < N and ARR[newY][newX]==3: #얘네가 갈 수 있는 길이면
#                 return 1
#             if 0<= newY < N  and 0<= newX < N and ARR[newY][newX]==0: #얘네가 갈 수 있는 길이면
#                 ST.append((newX, newY))
#                 ARR[newY][newX] = 1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst2 = [list(map(int, input())) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if lst2[y][x] == 2:
                start_x = x
                start_y = y
                break
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    answer = 0
    visited = [] # 스택
    DFS(start_y, start_x)
    print('#{} {}'.format(test_case, answer))



