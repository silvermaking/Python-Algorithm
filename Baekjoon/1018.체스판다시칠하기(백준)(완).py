def IsChess(lst):
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if lst[i][j] != chess1[i][j]:
                cnt1 += 1
            if lst[i][j] != chess2[i][j]:
                cnt2 += 1
    if cnt2 > cnt1:
        cnt = cnt1
    else:
        cnt = cnt2
    return cnt

N, M = map(int, input().split())
square = [input() for _ in range(N)]

chess1 = []
chess2 = []
for i in range(8):
    if i % 2:
        chess1.append('WB'*4)
        chess2.append('BW'*4)
    else:
        chess1.append('BW' * 4)
        chess2.append('WB' * 4)

rse = []
for a in range(0,M-7):
    for b in range(0, N-7):
        lst = []
        for j in range(b, b+8):
            lst.append(square[j][a:a+8])
        rse.append(IsChess(lst))

print(min(rse))
