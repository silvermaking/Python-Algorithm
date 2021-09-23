'''
완전 이진트리
후위탐색(post_order)
'''
def post_order(L):
    if L <= N:
        if not tree[L]:
            left = post_order(L*2)
            right = post_order(L*2 + 1)

            tree[L] = left + right

        return tree[L]
    return 0

for tc in range(1, int(input())+1):
    #N: 노드갯수, M: 리프노트 갯수, L: 노드번호
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for __ in range(M):
        node, num = map(int, input().split())
        tree[node] = num

    ans = post_order(L)
    print(f'#{tc} {ans}')