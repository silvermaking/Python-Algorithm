'''
M초의 시간 후 K개 완성

'''
# import sys
# sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    N_lst = list(map(int, input().split()))
    ans = 'Possible'
    cnt = 0
    for i in range(0, max(N_lst)+1):
        if i != 0 and i%M == 0:
            cnt += K
        if i in N_lst:
            if cnt >= N_lst.count(i):
                cnt -= N_lst.count(i)
            else:
                ans = 'Impossible'
                break

    print(f'#{tc} {ans}')

