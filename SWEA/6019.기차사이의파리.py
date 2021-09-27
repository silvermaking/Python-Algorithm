'''
D = 사이거리
A = 속력
B = 속력
F = 파리
'''
T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
  #시간 * 속력 = 거리
    dtc = 0
    t = D / (A+B)  # A, B가 만날 때까지의 시간
    dtc = F * t
    # 소수점 제한
    print(f'#{tc} {dtc:.6f}')

