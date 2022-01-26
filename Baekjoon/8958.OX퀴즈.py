for _ in range(int(input())):
    ox_list = input()
    ans = 0
    n = len(ox_list)
    i = 0
    score = 0
    while i < n:
        if ox_list[i] == 'O':
            score += 1
            ans += score
        else:
            score = 0
        i += 1
    print(ans)
