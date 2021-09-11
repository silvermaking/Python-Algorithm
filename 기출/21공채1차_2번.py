'''
양의정수 n
k진수

- 0소수0
- 소수0
- 0소수
- 오직 소수
- 소수는 0 포함 x

'''
# 진수 변환
def change(n, k):
    rse = ''
    while n > 0:
        n, mod = divmod(n, k)
        rse += str(mod)
    rse = rse[::-1]
    return rse
import math
def primeNum(str):
    n = int(str)
    cnt = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt += 1
            break
    if cnt:
        return False
    else:
        return True

a = '1018612012390512390'
a_list = []
b = ''
i = 0
while i<len(a):
    if a[i] != '0':
        b += a[i]
        i += 1
    else:
        a_list.append(b)
        b = ''
        while i< len(a) and a[i] == '0':
            i += 1
if len(b):
    a_list.append(b)

print(a_list)
answer = 0
for str in a_list:
    if int(str) > 1 and primeNum(str):
        answer += 1
print(answer)