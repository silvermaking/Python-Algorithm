A, B = map(int, input().split())
i = 1
length = 0
while length < B:
    length += i
    i += 1

lst = []
for j in range(1, i):
    lst.extend([j] * j)
print(sum(lst[A-1:B]))