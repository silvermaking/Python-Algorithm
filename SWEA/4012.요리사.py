'''
완전탐색
dfs이용
'''

def synergy(food):
    score = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            score += S[food[i]][food[j]] + S[food[j]][food[i]]
    return score

def dfs(idx, K):
    global ans
    a = []
    b = []
    if idx == N//2:
        for i in range(N):
            if visited[i]:
                a.append(i)
            else:
                b.append(i)
        score_a = synergy(a)
        score_b = synergy(b)
        score = abs(score_b - score_a)
        if score < ans:
            ans = score
            return
    for i in range(K, N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx+1, i+1)
            visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    # N : 식재료의 수
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    visited = [0 for _ in range(N)]
    dfs(0, 0)
    print(f'#{tc} {ans}')