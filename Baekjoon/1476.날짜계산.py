E, S, M = map(int, input().split())
ans = 1
e = s = m = 1
while True:
    if (e, s, m) == (E, S, M):
        print(ans)
        break

    ans += 1
    e += 1
    if e > 15:
        e = 1
    s += 1
    if s > 28:
        s = 1
    m += 1
    if m > 19:
        m = 1
