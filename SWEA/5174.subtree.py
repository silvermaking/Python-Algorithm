T = int(input())
def order(N):
    global cnt
    cnt += 1
    for t in tree[N]:
        order(t)

for tc in range(1, T+1):
    # E: 간선 갯수 # N:루트
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+2)]
    temp_list = input().split()
    for i in range(0, E*2, 2):
        #부모 : [왼쪽, 오른쪽] 자식
        tree[int(temp_list[i])].append(int(temp_list[i+1]))

    cnt = 0
    order(N)
    print(f'#{tc} {cnt}')