import sys
for test_case in range(1, 6):
    sys.stdin = open(f'7. 사과나무/in{test_case}.txt', "r")
    N = int(input())
    lst2 = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N//2+1):
        if i < N//2:
            for j in range(N//2-i, N//2+1+i):
                ans += lst2[i][j]
                ans += lst2[-(i+1)][j]
        elif i == N//2:
            ans += sum(lst2[i])
    print(f'#{test_case} {ans}')


'''

1 1 1 1 1 1 1
     111 
    11111
  2   i = 0   2 3
 123  i = 1   1 4
012345 i = 2  0 5

'''
