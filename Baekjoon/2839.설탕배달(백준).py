'''
dp
-----------------------------
수학적으로 접근
N = 3x + 5y
x+y = minS가 최소
N = 3* minS + 2* y

(N-2*y)/3 = minS  : 3으로 나누어떨어져야 함
'''
import sys
N = int(sys.stdin.readline())
minS = 0
# for - else 구문 사용
for minS in range(1, N//3+1):
    dpN = N - minS * 3
    if dpN % 2 == 0:
        y = dpN//2
        if y <= minS:
            print(minS)
            break
else:
    print(-1)