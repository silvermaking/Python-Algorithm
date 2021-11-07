"""
dp
=============
dp[1] = 1번 pack 1개
dp[2] = 2번 pack 1개, 1번 pack 2개
...
dp[n] = n번 pack 1개 or (dp[i] and dp[n-i])
"""


import sys
input = sys.stdin.readline

N = int(input())
packs = [0] + list(map(int, input().strip().split()))

dp = [0] * (N+1)
dp[1] = packs[1]
dp[2] = max(packs[2], packs[1]*2)

for i in range(3, N+1):
    dp[i] = packs[i]
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[N])