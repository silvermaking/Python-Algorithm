import sys
from collections import deque
import sys

input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    x = input().split()
    if x[0] == 'push':
        q.append(int(x[1]))
    elif x[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif x[0] == 'size':
        print(len(q))
    elif x[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif x[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)