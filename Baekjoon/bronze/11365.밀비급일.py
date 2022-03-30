import sys

input = sys.stdin.readline

while True:
    words = input().strip()
    if words == 'END':
        break
    print(words[::-1])