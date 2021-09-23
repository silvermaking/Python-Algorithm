'''
중위순회(in_order)
'''
#중위순회 알고리즘 이용
#tree만들기
def in_order(a):
    global cnt
    if a <= N:
        in_order(a*2)
        tree[a] = cnt
        cnt += 1
        in_order(a*2 + 1)


for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1
    in_order(1)
    print(tree)
    print(f'#{tc} {tree[1]} {tree[N//2]}')