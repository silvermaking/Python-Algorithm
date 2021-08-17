
for test_case in range(1, 11):
    tc = int(input())
    lst2 = [list(map(int, input().split())) for _ in range(100)]
    # 풀이 1
    posY = 99
    for i in range(100):
        if lst2[posY][i] != 2:
            continue

        posX = i
        while posY >= 0:
            posY -= 1
            if posX>0 and lst2[posY][posX-1] == 1: # 좌측에 1이 있으면
                while posX >0 and lst2[posY][posX-1] == 1:
                    posX -= 1

            elif posX<99 and lst2[posY][posX+1] == 1: # 우측에 1이 있으면
                while posX<99 and lst2[posY][posX+1] == 1:
                    posX += 1

        break
    print('#{} {}'.format(tc, posX))
    '''풀이 2
    row = 99
    for i in range(100):
        if lst2[row][i] == 2:
            col = i
            break
    while True:
        if row == 0:
            print(f'#{tc} {col}')
            break
        row -= 1
        if col > 0 and lst2[row][col-1] == 1:
            col -= 1
            while lst2[row-1][col] == 0:
                col -= 1
                if col == 0 or col == 99:
                    break

        elif col < 99 and lst2[row][col+1] == 1:
            col += 1
            while lst2[row-1][col] == 0:
                col += 1
                if col == 0 or col == 99:
                    break
    '''