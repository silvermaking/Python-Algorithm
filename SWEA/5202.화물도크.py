'''
greedy
'''
for tc in range(1, int(input()) + 1):
    #N : 신청서
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort() #시작시간으로 정렬
    start = lst.pop()[0] # 가장 늦은 시작시간
    cnt = 1
    while lst: # 모든 화물 돌리기
        s, e= lst.pop()
        if e <= start:
            start = s
            cnt += 1

    print(f'#{tc} {cnt}')