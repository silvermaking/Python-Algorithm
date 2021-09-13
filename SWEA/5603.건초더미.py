T = int(input())
for tc in range(1, T+1):
    N = int(input())
    guncho = [int(input()) for _ in range(N)]
    m = sum(guncho)//len(guncho)
    cnt = 0
    while True:
        if min(guncho) == m:
            break
        for i in range(len(guncho)):
            if guncho[i] < m:
                cnt += m - guncho[i]
                guncho[i] = m
                break
    print(f'#{tc} {cnt}')
'''
20 
5
2 10 7 1
2  9 7 2
2  8 7  3
3  7 7  3
4  6 7  3
4  6 6  4
5  5 5  4
5  5 5 5 
'''