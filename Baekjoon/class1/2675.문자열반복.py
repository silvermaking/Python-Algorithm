for _ in range(int(input())):
    R, S = input().split()
    R = int(R)
    new_s = ''
    for s in S:
        new_s += s * R

    print(new_s)