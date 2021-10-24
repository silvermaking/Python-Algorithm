"""
greedy : 가장 큰 것끼리 곱해나가자

"""
for tc in range(1, int(input()) + 1):
    N = int(input())
    biscuits = sorted(list(map(int, input().split())), reverse=True)
    canapes = sorted(list(map(int, input().split())), reverse=True)

    ans = 0
    for i in range(N):
        ans += biscuits[i] * canapes[i]

    print(f'#{tc} {ans}')
