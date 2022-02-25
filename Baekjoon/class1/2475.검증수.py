import sys

input = sys.stdin.readline

lst = list(map(int, input().strip().split()))
ans = 0
for a in lst:
    ans += a ** 2

print(ans % 10)