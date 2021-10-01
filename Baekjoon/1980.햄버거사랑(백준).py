'''
구현, brute-force

=======

'''
import sys
n, m, t = map(int, sys.stdin.readline().strip().split())
coke = 0
temp_t = t
cnt = 0
while True:
    #종료조건
    if temp_t == 0:
        break

    # 나누어 안떨어지면 coke 한개 씩 추가
    if temp_t < 0:
        coke += 1  #1분
        temp_t = t - coke  # 7분 -1분 = 6분
        cnt = 0
    #적은 타임의 햄버거수가 더 많게
    if n <= m:
        if temp_t % n == 0:
            cnt += temp_t // n
            temp_t = 0
        else:
            temp_t -= m
            cnt += 1
    else:
        if temp_t % m == 0:
            cnt += temp_t // m
            temp_t = 0
        else:
            temp_t -= n
            cnt += 1
print(f'{cnt} {coke}')