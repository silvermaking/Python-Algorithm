"""
부분집합
비트연산으로
"""
def powerset(lst):
    global cnt
    for i in range(1<<N): # 1을 좌측으로 N번 == 2**N
        temp = 0
        for j in range(N):
            if i & (1<<j): # i의 j번째 비트 검사, ex) 0101이랑 검사
                temp += lst[j]
                if temp > K: #시간 효율
                    break
        if temp == K:
            cnt += 1
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    N_lst = list(map(int, input().split()))

    cnt = 0
    powerset(N_lst)
    print(f'#{tc} {cnt}')