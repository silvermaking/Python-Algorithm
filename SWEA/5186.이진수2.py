for tc in range(1, int((input()))+1):
    N = float(input())

    i = 1/2
    answer = ''
    cnt = 1
    while True:
        #종료조건
        if cnt >= 13:
            answer = 'overflow'
            break
        if N == i:
            answer += '1'
            break
        elif N > i:
            answer += '1'
            N -= i
        else:
            answer += '0'

        cnt += 1
        i *= 1/2
    print(f'#{tc} {answer}')