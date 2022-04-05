from sys import stdin

def eratosthenes(m, n):
    memo = [1] * (n+1)

    for i in range(2, int(n**0.5) + 1):
        if memo[i]:
            for j in range(2*i, n+1, i):
                memo[j] = 0
    memo[:2] = 0, 0
    memo[:m] = [0] * m
    return memo

M, N = map(int, stdin.readline().split())
lst = eratosthenes(M, N)
for i in range(M, N+1):
    if lst[i]:
        print(i)
