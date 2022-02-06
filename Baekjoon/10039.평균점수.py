ans = 0
for _ in range(5):
    temp = int(input())
    if temp < 40:
        temp = 40
    ans += temp

print(ans // 5)