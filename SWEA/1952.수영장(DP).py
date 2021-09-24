'''
DP
'''
for tc in range(1, int(input())+1):
    # D: 1일 , M: 월, T: 3개월, Y : 1년
    D, M, T, Y = map(int, input().split())
    month = [0] + list(map(int, input().split()))

    dp = [0] * 13 # 해당 월까지의 최소값을 저장

    dp[1] = min(M, month[1] * D)
    dp[2] = dp[1] + min(M, month[2] * D)

    for i in range(3, 13):
        dp[i] = min(dp[i-3] + T, dp[i-1] + M, dp[i-1] + month[i] * D)

    print(f'#{tc} {min(dp[12], Y)}')