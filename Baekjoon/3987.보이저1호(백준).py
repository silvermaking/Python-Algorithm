"""
구현, 시뮬레이션
========================
방향대로 가면서 cnt 더해주는 건 구현
무한루프일 경우 탈출하는 알고리즘 => 루프가 전체 그래프 *2 넘어갈때
(좀더 좋은 알고리즘 생각해보기)

"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
s_y, s_x = map(int, input().split())
s_y, s_x = s_y - 1 , s_x - 1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
direction = ['U', 'R', 'D', 'L']
cnt_list = []
def solve():
    for i in range(4):
        cnt = 1
        tmp_y = s_y
        tmp_x = s_x
        tmp_dy = dy[i]
        tmp_dx = dx[i]
        while True:
            tmp_y = tmp_y + tmp_dy
            tmp_x = tmp_x + tmp_dx
            if not 0 <= tmp_y < N or not 0 <= tmp_x < M or graph[tmp_y][tmp_x] == 'C':
                break
            if graph[tmp_y][tmp_x] == '\\':
                tmp_dx, tmp_dy = tmp_dy, tmp_dx
            elif graph[tmp_y][tmp_x] == '/':
                tmp_dx, tmp_dy = -tmp_dy, -tmp_dx
            cnt += 1
            if cnt >= (N*M) * 2:
                return print(direction[i], 'Voyager', sep='\n')
        cnt_list.append(cnt)
    ans = max(cnt_list)
    ans_d = direction[cnt_list.index(ans)]
    return print(ans_d, ans, sep='\n')

solve()

