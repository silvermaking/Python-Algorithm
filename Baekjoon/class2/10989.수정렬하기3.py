import sys

input = sys.stdin.readline
T = int(input())
lst = [0] * 10001
for _ in range(T):
    lst[int(input())] += 1

for i in range(10001):
    if lst[i]:
        for j in range(lst[i]):
            print(i)