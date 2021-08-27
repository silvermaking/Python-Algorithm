def in_order(v):
    if v <= N:
        in_order(v*2)
        print(tree[v], end='')
        in_order(v*2 +1)

for tc in range(1, 11):
    N = int(input())
    tree = [[0] for _ in range(N+1)]
    for _ in range(N):
        node = input().split()
        tree[int(node[0])] = node[1]
    print(f'#{tc} ', end='')
    in_order(1)
    print()