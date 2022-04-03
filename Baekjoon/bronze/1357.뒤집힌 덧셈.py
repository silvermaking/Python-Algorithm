def rev(a):
    return a[::-1]


x, y = input().split()
temp = int(rev(x)) + int(rev(y))
ans = rev(str(temp))
print(int(ans))