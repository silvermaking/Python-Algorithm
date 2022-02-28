lst = list(map(int, input().split()))

as_list = [1, 2, 3, 4, 5, 6, 7, 8]
de_list = [8, 7, 6, 5, 4, 3, 2, 1]

if lst == as_list:
    print("ascending")
elif lst == de_list:
    print("descending")
else:
    print("mixed")