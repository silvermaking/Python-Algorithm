T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans_lst = [0] * 5
    a = [2, 3, 5, 7, 11]
    for i in range(len(a)):
        cnt = 0
        while True:
            if N%a[i]==0:
                N = N//a[i]
                cnt += 1
            else:
                ans_lst[i] += cnt
                break
    #출력
    print(f'#{tc} ', end='')
    for ans in ans_lst:
        print(ans, end=' ')
    print()

