T = int(input())
for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    # 111111
    HH = (11 * 60 + 11) + 11 * (60*24) # 7000분
    solo = (H * 60 + M) + D * (60*24)  # 7200분
    if solo >= HH:
        print(f'#{tc} {solo-HH}')
    else:
        print(f'#{tc} -1')
