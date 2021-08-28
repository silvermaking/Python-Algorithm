#완료
#수학적으로 풀었는데
#리스트로도 다시 풀어보기

N = int(input())
def fibo(n):
    if n<=2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
def judge(s):
    lst = [N, s]
    x = 1   # answer = x+1
    minus1 = 0
    while True:
        minus = (-1) ** minus1
        a = fibo(x) * minus
        b = fibo(x + 1) *minus
        if a * N - b * s>= 0:
            lst.append(a * N - b * s)
            x += 1
            minus1 += 1
        else:
            break
    return x, lst
maxX = 0
for i in range(N+1):
    x, lst = judge(i)
    if x > maxX:
        maxX = x
        ans_lst = lst

print(maxX + 1)
for ans in ans_lst:
    print(ans, end=' ')
print()