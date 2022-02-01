import sys
input = sys.stdin.readline

words = set()
N = int(input())
for _ in range(N):
    temp = input().strip()
    words.add(temp)

words = list(words)
words.sort(key= lambda x: [len(x), x])
for word in words:
    print(word)