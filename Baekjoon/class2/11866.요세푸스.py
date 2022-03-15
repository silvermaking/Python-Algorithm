from collections import deque

N, K = map(int, input().split())
ans_list = []
q = deque()
for i in range(1, N + 1):
    q.append(i)

while q:
    for i in range(K-1):
        q.append(q.popleft())
    ans_list.append(q.popleft())

print("<", end='')
for i in range(N - 1):
    print(f'{ans_list[i]}, ', end='')
print(f'{ans_list[-1]}>')