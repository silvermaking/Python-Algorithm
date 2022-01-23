number_list = list(input())
number_list.sort(reverse=True)
ans = ""
for number in number_list:
    ans += number
print(ans)