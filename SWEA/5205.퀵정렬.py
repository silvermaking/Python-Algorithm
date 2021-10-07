def partionL(lst, l, r):
    p = r
    i = l - 1
    for j in range(l, r):
        if lst[j] < lst[p]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[p], lst[i+1] = lst[i+1], lst[p]
    return i + 1
def quickSort(lst, l, r):
    if l < r:
        s = partionL(lst, l, r)
        quickSort(lst, l, s-1)
        quickSort(lst, s+1, r)

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    quickSort(lst, 0, N-1)
    print(f'#{tc} {lst[N//2]}')