import sys
for test_case in range(1, 6):
    sys.stdin = open(f'8. 곳감/in{test_case}.txt', "r")
    N = int(input())
    lst2 = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    M_lst = [list(map(int, input().split())) for _ in range(M)]
    for lst in M_lst:
        if lst[0] != 1 and lst[0] != N:
            if lst[1] == 0: #left
                l = lst[2] % N
                a = lst2[lst[0]-1][l:]
                a.extend(lst2[lst[0]-1][:l])
                lst2[lst[0]-1] = a
            elif lst[1] == 1: #right
                r = lst[2] % N
                b = lst2[lst[0]-1][N-r:]
                b.extend(lst2[lst[0]-1][:N-r])
                lst2[lst[0]-1] = b
    ans = 0
    for i in range(N//2+1):
        if i < N//2:
            for j in range(i, N-i):
                ans += lst2[i][j]
                ans += lst2[-(i+1)][j]
        elif i == N//2:
            ans += lst2[i][i]
    print(f'{test_case} {ans}')
'''
왼쪽 : 0 
오른쪽 : 1
'''