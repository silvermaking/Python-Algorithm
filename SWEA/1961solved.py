import sys
sys.stdin = open('input1961.txt', "r")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n_matrix = [list(input().split()) for _ in range(N)]
    '''
    1 2 3  첫번쨰 밑에서 위로
    4 5 6  두번째(180) 밑에서 위로, 우에서 좌로
    7 8 9  세번째(270) 위세서 아래로, 우에서 좌로
    '''
    answer = []
    for i in range(N):
        element90 = ''
        element180 = ''
        element270 = ''
        for j in range(N):
            element90 += n_matrix[-(j+1)][i]
            element180 += n_matrix[-(i+1)][-(j+1)]
            element270 += n_matrix[j][-(i+1)]

        lst = [element90, element180, element270]
        answer.append(lst)

    print('#{}'.format(test_case))
    for asr in range(N):
        print(' '.join(answer[asr]))