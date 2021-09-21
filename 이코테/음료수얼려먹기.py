'''
DFS

입력 예시
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

3 3
001
010
101
'''

# N, M 입력
N, M = map(int, input().split())
# 2차원 리스트
graph = [list(map(int, input())) for _ in range(N)]
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    #노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문처리
        graph[x][y] = 1
        # 상하좌우 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
