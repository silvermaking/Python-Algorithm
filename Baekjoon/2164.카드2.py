import sys
from collections import deque
input = sys.stdin.readline

def game(n):
    lst = [i for i in range(1, n+1)]
    q = deque(lst)

    while len(q) > 1:
        q.popleft()
        temp = q.popleft()
        q.append(temp)
    print(q[0])


N = int(input())
game(N)