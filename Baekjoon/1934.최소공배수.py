import sys

input = sys.stdin.readline

def gcd_get(x, y):
    if y == 0:
        return x
    return gcd_get(y, x % y)

for _ in range(int(input())):
    a, b = map(int, input().split())
    gcd = gcd_get(a, b)

    print((a * b) // gcd)