N = int(input())

ans = 1
if N == 0:
    ans = 1
else:
    for i in range(1, N+1):
        ans *= i

cnt = 0
dvd = 10
while True:
    x = ans % dvd
    if x:
        print(cnt)
        break
    cnt += 1
    dvd *= 10