"""
greedy
==============
모든 전봇대에 대해서 교차하는 경우 비교
2번씩 생기므로 마지막에 나누기(//) 2

"""

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if i == j: continue

            if lst[i][0] < lst[j][0] and lst[i][1] > lst[j][1]:
                cnt += 1

            if lst[i][0] > lst[j][0] and lst[i][1] < lst[j][1]:
                cnt += 1

    print(f'#{tc} {cnt // 2}')