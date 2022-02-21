N = int(input())
cycle = 0
ans = N
while True:
    if N < 10:
        x = int(str(N) + str(N))
    else:
        temp = (N//10 + N % 10) % 10
        x = int(str(N % 10) + str(temp))
    cycle += 1
    if x == ans:
        print(cycle)
        break
    N = x
