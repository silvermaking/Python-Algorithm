import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

print(lst[K-1])