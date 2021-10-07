def dfs(idx): # x축 퀸 판별
    global cnt
    if idx == N:
        cnt += 1
        return

    for y in range(N):
        if y in col or idx+y in r_diagonal or idx-y in l_diagonal:
            continue
        col.add(y)
        r_diagonal.add(idx+y)
        l_diagonal.add(idx-y)
        dfs(idx+1)
        col.remove(y)
        r_diagonal.remove(idx+y)
        l_diagonal.remove(idx-y)
for tc in range(1, int(input()) + 1):
    N = int(input())
    col, r_diagonal, l_diagonal = set(), set(), set() #직선으로 보기
    cnt = 0
    dfs(0)
    print(f'#{tc} {cnt}')