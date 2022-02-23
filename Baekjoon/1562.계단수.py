N = int(input())
di = 1000000000
dp = [[[0] * 10 for _ in range(101)] for _ in range(1 << 10)]

for i in range(1, 10):
    dp[1<<i][0][i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(1024):
            if j < 9:
                dp[k | (1 << j)][i][j] = (dp[k | (1 << j)][i][j] + dp[k][i-1][j+1]) % di
            if j > 0:
                dp[k | (1 << j)][i][j] = (dp[k | (1 << j)][i][j] + dp[k][i-1][j-1]) % di

print(sum(dp[1023][N-1]) % di)

