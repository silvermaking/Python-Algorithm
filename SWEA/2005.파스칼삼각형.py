
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    pascal = [[1 for _ in range(i)] for i in range(1, N + 1)]
    print(f'#{test_case}')
    for i in range(0, N):
        if i <= 1:
            print(' '.join(map(str, pascal[i])))
        else:
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            print(' '.join(map(str, pascal[i])))

