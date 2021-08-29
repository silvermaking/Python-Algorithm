#brute force
'''
0 1 2 3 4 5  (0,5) (1,3) (2,4) 마주보는 면
0 5 1 3 2 4
'''
def dice(x, lst): #x = 윗면  [[2, 4], [3, 6], [1, 5]]
    global answer
    dice_lst = []
    for i in range(3):
        if x not in lst[i]:
            dice_lst.append(max(lst[i]))
        else:
            if x == lst[i][0]:
                new_x = lst[i][1]
            else:
                new_x = lst[i][0]
    answer.append(max(dice_lst))
    return new_x
N = int(input())
lst2 = [list(map(int, input().split())) for _ in range(N)]
New_lst = [[] for _ in range(N)]
for i in range(N):
    New_lst[i].append([lst2[i][0], lst2[i][5]])
    New_lst[i].append([lst2[i][1], lst2[i][3]])
    New_lst[i].append([lst2[i][2], lst2[i][4]])

answer = []
result = []
for i in range(6):
    x = lst2[0][i] #첫주사위 임의의 윗면
    j = 0
    while j<N:
        x = dice(x, New_lst[j])
        j += 1
    result.append(sum(answer))
    answer = []
print(max(result))



