'''
D = 사이거리
A = 속력
B = 속력
F = 파리
'''
T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    dtc = 0
    t = D / (A+B)  # A, B가 만날 때까지의 시간
    dtc = F * t
    print(f'#{tc} {dtc}')
    # 마지막말 무슨 말인지 모르겠다