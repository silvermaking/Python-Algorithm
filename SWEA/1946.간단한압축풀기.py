T = int(input())
for tc in range(1, T+1):
    N = int(input())
    answer = ''
    for _ in range(N):
        C, K = input().split()
        answer += C * int(K)
    print(f'#{tc}')
    i = 0

    while i < len(answer):
        print(answer[i:i+10])
        i += 10

