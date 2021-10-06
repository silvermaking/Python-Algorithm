def msort(arr):
    global cnt
    #종료조건
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left_arr = msort(arr[:mid])
    right_arr = msort(arr[mid:])

    if left_arr[-1] > right_arr[-1]:
        cnt += 1

    tmp_arr = []
    l = h = 0
    while l < len(left_arr) and h < len(right_arr):
        if left_arr[l] < right_arr[h]:
            tmp_arr.append((left_arr[l]))
            l += 1
        else:
            tmp_arr.append(right_arr[h])
            h += 1
    tmp_arr += left_arr[l:]
    tmp_arr += right_arr[h:]
    return tmp_arr

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    m_lst = msort(lst)

    #출력 : n//2 , cnt
    print(f'#{tc} {m_lst[N//2]} {cnt}')