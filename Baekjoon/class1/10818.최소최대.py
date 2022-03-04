import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().strip().split()))

print(min(numbers), max(numbers))