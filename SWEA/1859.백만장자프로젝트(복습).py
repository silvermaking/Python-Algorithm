T = int(input())
# 방법1 : for문 뒤에서부터 돌리기
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    maxV = lst[-1]
    for i in range(N-2, -1, -1):
        if maxV >= lst[i]:
            ans += maxV-lst[i]
        else:
            maxV = lst[i]

    print(f'#{tc} {ans}')
#방법2 : lst를 뒤부터 받기
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))[::-1]
#     ans = 0
#     maxV = lst[0]
#     for i in range(1, N):
#         if maxV >= lst[i]:
#             ans += maxV-lst[i]
#         else:
#             maxV = lst[i]
#
#     print(f'#{tc} {ans}')