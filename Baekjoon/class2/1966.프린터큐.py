from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx = deque(range(len(q)))
    idx[M] = 'target'
    cnt = 0
    while q:
        x = q[0]
        if x == max(q):
            cnt += 1
            if idx[0] == 'target':
                print(cnt)
                break
            else:
                q.popleft()
                idx.popleft()
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())
