import sys
for test_case in range(1, 6):
    sys.stdin = open(f'9. 봉우리/in{test_case}.txt', "r")
    N = int(input())
    lst2 = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        lst2[i].insert(N, 0)
        lst2[i].insert(0, 0)
    lst2.insert(N, [0]*(N+2))
    lst2.insert(0, [0]*(N+2))
    for i in range(1, len(lst2)-1):
        for j in range(1, len(lst2)-1):
            a = lst2[i][j]
            if a>lst2[i-1][j] and a>lst2[i+1][j] and a>lst2[i][j-1] and a>lst2[i][j+1]:
                cnt += 1

    print(f'#{test_case} {cnt}')


