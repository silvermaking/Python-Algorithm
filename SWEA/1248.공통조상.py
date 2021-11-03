from collections import deque

for tc in range(1, int(input()) + 1):
    V, E, s1, s2 = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [0] * (V + 1)
    for i in range(0, len(lst), 2):
        a, b = lst[i], lst[i+1]
        tree[b] = a
    parent1 = [s1]
    parent2 = [s2]
    while tree[s1]:
        parent1.append(tree[s1])
        s1 = tree[s1]

    while tree[s2]:
        parent2.append(tree[s2])
        s2 = tree[s2]

    i = len(parent1) - 1
    j = len(parent2) - 1

    while parent1[i] == parent2[j]:
        i -= 1
        j -= 1

    ans = parent1[i+1]
    cnt = 1
    q = deque()
    q.append(ans)

    while q:
        a = q.popleft()
        for i in range(1, len(tree)):
            if tree[i] == a:
                q.append(i)
                cnt += 1

    print(f'#{tc} {ans} {cnt}')