def chk(lst, key):
    '''
    찾으면 1,  아니면 0
    조건이 안 맞는 경우도 0
    '''
    l = 0
    r = len(lst) - 1
    di = 0 # 방향 체크
    while l <= r:
        m = (l+r) // 2
        if lst[m] == key:
            return 1

        if key < lst[m]:
            if di == 'L':
                return 0
            r = m - 1  # r이동
            di = 'L'
        else:
            if di == 'R':
                return 0
            l = m + 1  # l 이동
            di = 'R'
    return 0

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for b in B:
        cnt += chk(A, b)

    print(f'#{tc} {cnt}')