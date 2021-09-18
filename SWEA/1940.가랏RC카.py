T = int(input())
for tc in range(1, T+1):
    N = int(input())
    v = 0
    distance = 0
    for _ in range(N):
        s = list(map(int, input().split()))
        if s[0] == 1:
            v += s[1]
        elif s[0] == 2:
            v -= s[1]
            if v <= 0:
                v = 0
        distance += v
    print(f'#{tc} {distance}')