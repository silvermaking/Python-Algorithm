def solve(k, remain, cnt):
    global minC
    if minC <= cnt: #backtracking
        return
    if k == lst[0]:
        if minC > cnt:
            minC = cnt
        return

    if remain == 0: return
    solve(k+1, lst[k+1], cnt+1)
    solve(k+1, remain-1, cnt)

for tc in range(1, int(input()) + 1):
    lst = list(map(int, input().split())) +[0]
    minC = 101
    solve(1, lst[1], 0)
    print(f'#{tc} {minC}')