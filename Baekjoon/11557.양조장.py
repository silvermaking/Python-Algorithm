for _ in range(int(input())):
    N = int(input())
    c_list = []
    a_list = []
    for _ in range(N):
        college, alcohol = input().split()
        c_list.append(college)
        a_list.append(int(alcohol))

    print(c_list[a_list.index(max(a_list))])

