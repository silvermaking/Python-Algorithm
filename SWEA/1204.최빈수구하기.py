def my_max(lst):
    maxV = 0
    for i in range(len(lst)):
        if lst[i] >= maxV:
            maxV = lst[i]
            pos = i
    return pos

T = int(input())
for _ in range(T):
    tc = int(input())
    scores = list(map(int, input().split()))
    ans_lst = [0] * 101 # 점수 현황판, 0~100
    for score in scores:
        ans_lst[score] += 1

    ans = my_max(ans_lst)
    print(f'#{tc} {ans}')