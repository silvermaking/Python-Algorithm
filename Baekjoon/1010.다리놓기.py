"""
수학 : 조합
메모이제이션
"""

import sys
input = sys.stdin.readline


def factorial(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(n * factorial(n-1))
    return memo[n]


memo = [1, 1]
for _ in range(int(input())):
    r, n = map(int, input().strip().split())
    print(int(factorial(n) /(factorial(r) * factorial(n-r))))
