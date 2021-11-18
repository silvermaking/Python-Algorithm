"""
구현
1. 일단 숫자를 만들 수 있는지 (string으로 변환해서)
2. 숫자의 조합으로 나눠지는지
3. 나눠지면 재귀, 안 나눠지면 (min_cnt 변화없으면)

"""
import sys
sys.stdin = open("input1808.txt", "r")

#3
def per(x, k, num, per_list):
    if k == x:
        per_list.append(num)
        return

    for i in range(len(p_list)):
        if k == 0 and p_list[i] == "0": continue
        per(x, k+1, int(str(num) + p_list[i]), per_list)

def solve(cnt, str_X):
    global min_cnt
    if cnt >= min_cnt:
        return
    # 1
    i = 0
    while i < len(str_X):
        if str_X[i] in p_list:
            i += 1
        else:
            break
    if i == len(str_X):
        if cnt + i + 1 < min_cnt:
            min_cnt = cnt + i + 1
            return

    #2
    length = len(str_X)
    x = int(str_X)
    for i in range(1, length + 1):
        per_list = []
        per(i, 0, 0, per_list)
        for y in per_list:
            if y == 0 or y == 1 or y > x or x % y: continue
            if x == y:
                if cnt + 1 + i < min_cnt:
                    min_cnt = cnt + 1 + i
                return
            solve(cnt + 1 + i, str(x//y))

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for tc in range(1, int(input()) + 1):
    lst = list(map(int, input().split()))
    X = int(input())
    str_X = str(X)
    p_list = []

    min_cnt = 987654321
    for i in range(len(lst)):
        if lst[i]:
            p_list.append(str(num_list[i]))

    solve(0, str_X)
    #3
    if min_cnt == 987654321:
        min_cnt = -1

    print(f'#{tc} {min_cnt}')

