N = int(input())

length = len(str(N))
x = N - length * 9
if x < 0:
    x = 1

for i in range(x, N + 1):
    temp = sum(map(int, str(i)))
    m = i + temp
    if m == N:
        print(i)
        break
    if i == N:
        print(0)
