#queue
#화덕이 다돌고 그다음에 들어옴
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N:화덕크기, M:피자 개수
    cheese = list(map(int, input().split()))
    q = []
    for i in range(N):
        q.append([i, cheese[i]]) # [피자번호, 치즈수]
    i = 0
    while len(q) != 1:
        p, c = q.pop(0)
        c = c // 2
        if c == 0:
            if N+i < M:
                q.append([N+i, cheese[N+i]])
                i += 1
        else:
            q.append([p, c])
    print(f'#{tc} {q[0][0]+1}')
