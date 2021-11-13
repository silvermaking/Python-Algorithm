"""
2, 3 ,5 ,7 , 11, 13, 17, 19, 23, 29
적어도
=> 1 - 두팀다 소수 아닌 확률

"""
def factorial(n):
    global memo
    if n > 1 and len(memo) <= n:
        memo.append(factorial(n-1) * n)
    return memo[n-1]

def comb(x, y):
    return factorial(x) / (factorial(x-y) * factorial(y))

lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
memo = [1]
for tc in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    a, b = A/100, B/100
    p_a, p_b = 0, 0
    for i in range(len(lst)):
        tmp_a, tmp_b = 1, 1
        p_a += comb(30, lst[i]) * (a**lst[i]) * ((1-a) ** (30 - lst[i]))
        p_b += comb(30, lst[i]) * (b**lst[i]) * ((1-b) ** (30 - lst[i]))

    ans = 1 - (1-p_a) * (1-p_b)
    print(f'#{tc} {ans:.5f}')