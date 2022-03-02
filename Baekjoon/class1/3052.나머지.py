mod = 42
numbers = [int(input()) for _ in range(10)]
ans = []

for num in numbers:
    temp = num % mod
    if temp not in ans:
        ans.append(temp)

print(len(ans))