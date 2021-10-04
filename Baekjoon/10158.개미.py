'''
x,y 따로 생각
벽찍고 반대방향으로
몫이 짝수면 나머지가 그래프에 있는 값
몫이 홀수면 나머지는 그래프에서 반대부터 있는 값
'''

import sys
# w, h
w, h = map(int, sys.stdin.readline().split())
# p, q
p, q = map(int, sys.stdin.readline().split())
# 시간 t
t = int(sys.stdin.readline())

p += t
q += t
a, b = divmod(p, w)
c, d = divmod(q, h)
if a%2:
    p = w - b
else:
    p = b
if c%2:
    q = h - d
else:
    q = d

print(p, q)

