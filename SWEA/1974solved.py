def SolveSudoku(sudoku):
    for i in range(9):
        lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if sudoku[i][j] in lst1:
                lst1.remove(sudoku[i][j])
            else:
                return 0
            if sudoku[j][i] in lst2:
                lst2.remove(sudoku[j][i])
            else:
                return 0
    x = 0
    while x < 9:
        lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(x, x + 3):
            for j in range(0, 3):
                if sudoku[i][j] in lst3:
                    lst3.remove(sudoku[i][j])
                else:
                    return 0
        lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(x, x + 3):
            for j in range(3,6):
                if sudoku[i][j] in lst3:
                    lst3.remove(sudoku[i][j])
                else:
                    return 0
        lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(x, x + 3):
            for j in range(6, 9):
                if sudoku[i][j] in lst3:
                    lst3.remove(sudoku[i][j])
                else:
                    return 0
        x += 3
    return 1

T = int(input())
for test_case in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'#{test_case} {SolveSudoku(sudoku)}')