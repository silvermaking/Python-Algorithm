T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))[::-1] #뒤로부터 받기 .reverse()효과
    max_n = n_list[0]
    rse = 0
    for i in range(1, N):
        if max_n > n_list[i]:
            rse += max_n - n_list[i]
        else:
            max_n = n_list[i]
    print('#{} {}'.format(test_case, rse))