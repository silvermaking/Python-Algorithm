'''
dfs
- 음료수얼려먹기랑 비슷
- dfs세기 위해 cnt 리스트 생성
'''
import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def dfs(x, y, cnt):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        cnt.append(1)
        graph[x][y] = 0
        dfs(x-1, y, cnt)
        dfs(x+1, y, cnt)
        dfs(x, y-1, cnt)
        dfs(x, y+1, cnt)
        return True
    return False

result = 0

cnt = []
lst = []
for i in range(N):
    for j in range(N):
        if dfs(i, j, cnt):
            result += 1
            lst.append(sum(cnt))
            cnt = []
lst.sort()
print(result)
for c in lst:
    print(c)