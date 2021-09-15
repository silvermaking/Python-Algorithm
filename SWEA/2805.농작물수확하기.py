T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 1~ 49 홀수
    harvest = [list(map(int, input())) for _ in range(N)]
    m = N//2 # 중간위치
    cnt = 0
    for i in range(m):
        lst1 = harvest[i][m-i:m+1+i]
        lst2 = harvest[-1-i][m-i:m+1+i]
        cnt += sum(lst1)
        cnt += sum(lst2)
    cnt += sum(harvest[m])

    print(f'#{tc} {cnt}')