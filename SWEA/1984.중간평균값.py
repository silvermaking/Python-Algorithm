T = int(input())

for tc in range(1, T+1):
    lst = sorted(list(map(int, input().split())))
    minV = lst[0]
    maxV = lst[-1]
    cnt = 10
    sum_all = 0
    for i in lst:
        if i != minV and i != maxV:
            sum_all += i
        else:
            cnt -= 1

    mean = round(sum_all/cnt)
    print(f'#{tc} {mean}')
