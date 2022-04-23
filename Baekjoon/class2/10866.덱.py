import sys
from collections import deque

input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    x = list(input().split())
    order = x[0]
    if order == 'push_front':
        q.appendleft(x[1])
    elif order == 'push_back':
        q.append(x[1])
    elif order == 'pop_front':
        print(q.popleft()) if q else print(-1)
    elif order == 'pop_back':
        print(q.pop()) if q else print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'front':
        print(q[0]) if q else print(-1)
    elif order == 'back':
        print(q[-1]) if q else print(-1)
    else:
        print(0) if q else print(1)

