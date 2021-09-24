def calc(cost, m):
    global min_cost
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return
    #1일권
    calc(cost + D * lst[m], m + 1)
    #1달권
    calc(cost + M, m + 1)
    #3달권
    calc(cost + T, m + 3)

for tc in range(1, int(input())+1):
    # D: 1일 , M: 월, T: 3개월, Y : 1년
    D, M, T, Y = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    min_cost = Y
    calc(0, 1)
    print(f'#{tc} {min_cost}')