'''
greedy

'''

for tc in range(1, int(input()) + 1):
    #N :컨테이너 수, M : 트럭 수
    N, M = map(int, input().split())
    # N개의 화물 무게
    N_lst = list(map(int, input().split()))
    N_lst.sort(reverse=True)
    # M 트럭의 적재용량
    M_lst = list(map(int, input().split()))
    M_lst.sort(reverse=True)
    total = 0
    for n in N_lst:
        for i in range(len(M_lst)):
            if n <= M_lst[i]:
                total += n
                M_lst.pop(i)
                break

    print(f'#{tc} {total}')