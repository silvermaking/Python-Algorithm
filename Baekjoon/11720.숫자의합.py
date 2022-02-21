N = int(input())
numbers = input()
ans = 0

for num in numbers:
    if num != '0':
       ans += int(num)

print(ans)