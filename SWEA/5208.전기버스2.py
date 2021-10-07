'''
교환횟수가 최소
백트래킹, dfs
'''
def dfs(idx, cnt):
    global answer
    if answer < cnt: return # 백트래킹
    if idx >= N:
        answer = cnt
        return
    # 충전 최대값부터 역순으로 dfs
    for i in range(lst[idx], 0, -1):
        dfs(idx+i, cnt + 1)

for tc in range(1, int(input()) + 1):
    lst = list(map(int, input().split()))
    N = lst.pop(0) - 1
    answer = 987654321
    dfs(0, -1) # 첫번째꺼는 안 세서 -1
    print(f'#{tc} {answer}')