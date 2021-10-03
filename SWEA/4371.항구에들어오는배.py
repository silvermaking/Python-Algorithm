for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    visited = [0] * N
    ship = lst[1] - lst[0]
    cnt = 0 # 배 갯수
    while True:
        ST = [lst[0]]
        for i in range(1, N):
            if lst[i] - ST[-1] == ship:
                ST.pop()
                ST.append(lst[i])
                visited[i] = 1

        cnt += 1
        for j in range(1, N):
            if visited[j] == 0:
                ship = lst[j] - lst[0]
                break
        else:
            break
    print(f'#{tc} {cnt}')






