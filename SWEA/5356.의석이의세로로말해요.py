T = int(input())
for test_case in range(1, T+1):
    words = [input() for _ in range(5)]
    answer = ''
    maxV = 0
    for i in range(5):
        if len(words[i]) > maxV:
            maxV = len(words[i])

    for i in range(maxV):
        a = ''
        for j in range(5):
            a += words[j][i:i+1]
        answer += a

    print('#{} {}'.format(test_case, answer))