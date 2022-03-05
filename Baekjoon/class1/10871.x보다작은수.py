import sys

input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().strip().split()))

for a in A:
    if a < X:
        print(a, end=' ')