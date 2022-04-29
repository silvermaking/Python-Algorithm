import math


def is_prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return False
    return True


M = int(input())
N = int(input())
ans_sum = 0
for i in range(N, M-1, -1):
    if is_prime_num(i):
        ans_sum += i
        min_prime = i
if ans_sum:
    print(ans_sum, min_prime, sep='\n')
else:
    print(-1)