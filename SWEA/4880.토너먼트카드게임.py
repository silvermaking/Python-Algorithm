def RCP(g1, g2):
    l, r = students[g1-1], students[g2-1]
    if l == r:
        return g1
    elif (l, r) == (1, 3) or (l, r) == (2, 1) or (l, r) == (3, 2):
        return g1
    else:
        return g2
def game(i, j):
    if i == j: #종료조건
        return i
    group1 = game(i, (i+j)//2)
    group2 = game((i+j)//2 +1, j)
    return RCP(group1, group2)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    students = list(map(int, input().split()))
    print(f'#{test_case} {game(1, N)}')
