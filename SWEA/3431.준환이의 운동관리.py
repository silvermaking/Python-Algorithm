T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    # L분 이상 U분 이하
    #X분 운동
    ans = 0
    if X < L:
        ans = L - X
    elif U < X:
        ans = -1
    print(f'#{tc} {ans}')
