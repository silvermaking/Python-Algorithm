x, y = map(int, input().split())
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31 ,30 ,31]
lst2 = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
ans = 0

for i in range(x-1):
    ans += lst[i]

ans += y
print(lst2[ans % 7])
