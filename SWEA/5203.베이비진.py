def check(player, num):
    if player[num] == 3: #triplet
        return True
    cnt = 0
    for value in player.values():
        if value:
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 0
    return False
for tc in range(1, int(input()) + 1):
    nums = list(map(int, input().split()))
    # player a, b
    a = {i:0 for i in range(10)}
    b = {i:0 for i in range(10)}
    answer = 0
    for i in range(12):
        if i%2: #홀수일때
            b[nums[i]] += 1
            if check(b, nums[i]):
                answer = 2
                break
        else:
            a[nums[i]] += 1
            if check(a, nums[i]):
                answer = 1
                break

    print(f'#{tc} {answer}')