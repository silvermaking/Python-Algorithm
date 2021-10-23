"""
구현
=======================================
a : 정연이 부터 선택
b : 현용이
행복도선택 logic : a - (-b)
- happy를 행복도합순으로 정렬
- 해당하는 idx값에 해당하는 a, b를 정연히 현용이 번갈아 ans에 더해주거나 빼주기
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a_list = []
    b_list = []
    happy = []
    for idx in range(N):
        a, b = map(int, input().split())
        # 행복도, 행복도합
        a_list.append(a)
        b_list.append(b)
        happy.append([a+b, idx])

    happy.sort(key=lambda x: x[0], reverse=True)
    ans = 0
    for i in range(0, N):
        if i % 2:
            ans -= b_list[happy[i][1]]
        else:
            ans += a_list[happy[i][1]]

    print(f'#{tc} {ans}')
