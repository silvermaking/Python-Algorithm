# memory error
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))
    start_n = 0
    pos_n = 0
    rse = 0
    while True:
        n_list = n_list[start_n:]
        if len(n_list) == 0:
            break
        # max_n, pos_n = my_max_pos(n_list)
        max_n = max(n_list)
        pos_n = n_list.index(max_n)
        if pos_n:
            #OOM
            # for i in range(pos_n):
            #     rse += n_list[pos_n] - n_list[i]
            sum_n = sum(n_list[:pos_n])
            SUM_n = n_list[pos_n] * len(n_list[:pos_n])
            rse += SUM_n - sum_n
        start_n = pos_n + 1
    print('#{} {}'.format(test_case, rse))
