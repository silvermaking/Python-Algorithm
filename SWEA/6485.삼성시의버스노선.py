import sys
sys.stdin = open('s_input.txt', "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    # p가 차례대로 주어지는게 아님
    P_list = [int(input()) for _ in range(P)]
    answer = [0] * (5001)
    for i in range(N):
        for j in range(N_list[i][0], N_list[i][1]+1):
            answer[j] += 1

    for p in P_list:
       awr.append(answer[p])
    print('#{}'.format(test_case), *awr)

