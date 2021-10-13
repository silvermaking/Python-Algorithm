for tc in range(1, int(input()) + 1):
    # N : 학생 수 K : 과제 제출한 수
    N, K = map(int, input().split())
    # 과제 제출하지 않은 사람
    K_lst = list(map(int, input().split()))
    answer = [i for i in range(1, N+1) if i not in K_lst]
    print(f'#{tc}', end=" ")
    print(*answer)
