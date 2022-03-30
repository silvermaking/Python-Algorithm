lst = list(map(int, input().split()))
lst.sort()
ABC = input()
dic = {'A': lst[0], 'B': lst[1], 'C': lst[2]}

for i in ABC:
    print(dic[i], end=' ')

