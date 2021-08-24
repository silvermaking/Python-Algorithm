#백트래킹(순열)

import sys
sys.stdin = open('sample_input.txt', 'r')

def per(x):
    global minV, sumV # 값을 변경하고 싶을 때는 global 사용
    if minV < sumV: # backtracking
        return
    if x==N:
        if minV > sumV:
            minV = sumV
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            sumV += lst2[x][i]
            per(x+1)
            visited[i] = False
            sumV -= lst2[x][i]
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst2 = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    sumV, minV = 0, 10*N
    per(0)

    print(f'#{test_case} {minV}')

#교수님 풀이
def per1(x, sumV):
    global minV # 값을 변경하고 싶을 때는 global 사용
    if minV < sumV: # backtracking
        return
    if x==N:
        if minV > sumV:
            minV = sumV
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            per(x+1, sumV + lst2[x][i])
            visited[i] = False
