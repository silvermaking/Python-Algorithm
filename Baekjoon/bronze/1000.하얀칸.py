graph = [list(input()) for _ in range(8)]
ans = 0

for i in range(8):
    if i % 2:
        for j in range(1, 8, 2):
            if graph[i][j] == 'F':
                ans += 1
    else:
        for j in range(0, 7, 2):
            if graph[i][j] == 'F':
                ans += 1

print(ans)
