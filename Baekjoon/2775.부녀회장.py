import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input()) # 층
    n = int(input()) # 호
    arr = [[] for _ in range(k)]
    for j in range(1, n + 1):
        arr[0].append(j)
    for i in range(1, k):
        for j in range(1, n+1):
            arr[i].append(sum(arr[i-1][:j]))

    print(sum(arr[-1][:n]))

