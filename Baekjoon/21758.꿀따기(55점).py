'''
greedy
벌이 있는 곳은 못땀 : 2곳
벌(고정)  벌: 2번째부터 최대가 되는 곳  벌통(고정)
9 9 4 1 4 9 9
4 1 4 9  - 9 : 9
1 4 9 - 4    : 10
4 9   - 1    : 12
벌(고정) 벌통: 가장 큰수에 위치(x2)   벌(고정)
벌통(고정) 벌(2번쨰부터) 벌(고정)
'''
def my_max(x):
    if x > total:
        return x
    else:
        return total

import sys
N = int(sys.stdin.readline())
honey = list(map(int, sys.stdin.readline().split()))
total = 0
#벌통의 위치 기준

bee = 0
for i in range(1, N-1):
    temp = sum(honey[i+1:]) - honey[i]
    if bee <= temp:
        bee = temp
total = my_max(bee + sum(honey[1:]))

# 벌통 벌벌
honey = honey[::-1]
bee = 0
for i in range(1, N-1):
    temp = sum(honey[i+1:]) - honey[i]
    if bee <= temp:
        bee = temp
total = my_max(bee + sum(honey[1:]))
#벌 벌통 벌
answer = my_max(sum(honey[1:-1]) + max(honey[1:-1]))
print(answer)




