graph = [[0] * 100 for _ in range(100)]
ans = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x - 1, x + 9):
        for j in range(y - 1, y + 9):
            graph[i][j] = 1

for g in graph:
    ans += sum(g)

print(ans)