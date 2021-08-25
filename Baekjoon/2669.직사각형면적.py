#완료
lst2 = [[0]*101 for _ in range(101)] #좌표가 100까지 있으므로

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            lst2[x][y] = 1
answer = 0
for i in range(101):
    answer += sum(lst2[i])

print(answer)