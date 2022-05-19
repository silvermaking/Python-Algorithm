import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    words = list(input().split())
    for i in range(len(words)):
        tmp = words[i]
        words[i] = tmp[::-1]

    print(*words)