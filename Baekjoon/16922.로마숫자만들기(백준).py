import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            m = N - i - j - k
            roma_sum = i * 1 + j * 5 + k * 10 + m * 50
            lst.append(roma_sum)

print(f'{len(set(lst))}')
