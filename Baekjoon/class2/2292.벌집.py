"""
1, 6, 12, 18, 24,
1 7 19
"""
N = int(input())
d = 6
i = 1
x = 1
while True:
    x += d * (i - 1)
    if N <= x:
        print(i)
        break
    i += 1
