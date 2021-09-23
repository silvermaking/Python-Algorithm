def min_heap(node):
    if node//2 <= 0: #부모노드가 없으면
        return
    # 부모노드값이 크면 값 change
    if tree[node//2] > tree[node]:
        tree[node//2], tree[node] = tree[node], tree[node//2]
        # 조상노드 확인(재귀)
        min_heap(node//2)

for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0]
    node_num = 1
    for i in map(int, input().split()):
        tree.append(i)
        min_heap(node_num)
        node_num += 1

    ans = 0
    while N: #마지막 노드의 부모노드들 찾아가기
        N = N//2
        ans += tree[N]
    print(f'#{tc} {ans}')