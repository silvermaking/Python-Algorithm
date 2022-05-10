import sys

input = sys.stdin.readline
S = set()
for _ in range(int(input())):
    order = input().split()
    if order[0] == "add":
        S.add(order[1])
    elif order[0] == "check":
        if order[1] in S:
            print(1)
        else:
            print(0)

    elif order[0] == "remove":
        if order[1] not in S: continue
        S.remove(order[1])
    elif order[0] == "toggle":
        if order[1] in S:
            S.remove(order[1])
        else:
            S.add(order[1])
    elif order[0] == "all":
        S = {'11', '14', '9', '10', '4', '5', '18', '17', '12', '1', '8', '15', '6', '20', '16', '13', '2', '19', '7', '3'}
    else:
        S = set()