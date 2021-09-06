T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    m = (m1 + m2)%60
    h = (h1 + h2 + (m1+m2)//60)%12
    if h == 0:
        h = 12
    print(f'#{tc} {h} {m}')