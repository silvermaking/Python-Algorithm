import math


def isPrime(n):
    if n <=2:
        if n == 2:
            return True
        else:
            return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True

N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if isPrime(i):
        cnt += 1

print(cnt)


