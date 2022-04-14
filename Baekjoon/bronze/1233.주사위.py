s1, s2, s3 = map(int, input().split())

lst = [0] * 81
for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            lst[i + j + k] += 1

print(lst.index(max(lst)))
