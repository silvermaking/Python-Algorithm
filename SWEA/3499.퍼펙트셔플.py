T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_lst = list(input().split())
    ans = [''] * (N+1)

    if N%2:
        a = N//2 + 1
    else:
        a = N//2
    i = 0
    j = 1
    while i < N:
        if i < a:
            ans[i*2] += N_lst[i]
        else:
            ans[j] += N_lst[i]
            j += 2
        i += 1
    print(f'#{tc} ', end='')
    print(*ans)