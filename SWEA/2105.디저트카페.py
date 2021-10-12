'''
완전탐색

방향은
우하단(1,1) ->좌하단(1,-1) -> 좌상단(-1,-1) -> 우상단(-1, 1) 으로 고려
하나만 고려해도 되는 이유는 반대로 돌아도 순서만 바뀜

'''

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
def solve(i, j, k, n):
    '''
    :param x: 좌표 값
    :param y: 좌표 값
    :param k: 방향 ,방향이 3이면 사각형만듬
    :param n: 진행한 칸수
    :return:
    '''
    global start_i, start_j, ans
    #출발점에 사각형을 그리고 도착할 경우
    if k == 3 and i == start_i and j == start_j:
        if ans < n:
            ans = n
    #범위를 벗어날 경우
    elif not 0 <= i < N or not 0 <= j < N:
        return

    #같은 숫자를 지날 경우
    elif dessert[i][j] in visited:
        return
    else:
        visited.append(dessert[i][j])
        if k == 0 or k == 1:
            solve(i + dx[k], j + dy[k], k, n+1)
            solve(i + dx[k+1], j + dy[k+1], k+1, n+1)
        elif k == 2: #좌상단, 출발점으로 못감
            #우상단에 없을 경우
            if (i+j) != (start_i + start_j):
                solve(i + dx[k], j + dy[k], k, n+1)
            else:
                solve(i + dx[k+1], j + dy[k+1], k+1, n+1)
        else: #k == 3 일때, 직진하면 출발점 도착할 수 있다.
            solve(i + dx[k], j + dy[k], k, n+1)

        visited.remove(dessert[i][j])
T = int(input())
for tc in range(1, T + 1):
    # N : 한 변의 길이
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    visited = []
    for i in range(N):
        for j in range(N-1):
            start_i = i
            start_j = j
            visited.append(dessert[i][j])
            solve(i+1, j+1, 0, 1)
            visited.remove(dessert[i][j])
    print(f'#{tc} {ans}')