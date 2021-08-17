#queue stack
T = int(input())
for test_case in range(1, T+1):
    a = input()
    b = a.replace('()', 'R')
    tmp = 0
    ans = 0
    for i in b:
        if i == '(':  # 막대수 누적
            tmp += 1
        else:
            if i == 'R': #레이저 지나면 누적값 더하기
                ans += tmp
            else:  # 막대 끝나면 누적값-1 ans값 +1
                tmp -= 1
                ans += 1
    print('#{} {}'.format(test_case, ans))

 '''   메모리 아웃
 a = input()
    b = a.replace('()', 'R')
    i = 0
    cnt = 0
    x = 1
    length = 3
    while True:
        if len(b) == b.count('R'):
            break
        while True:
            if '('+ 'R'*x +')' not in b:
                break
            if b[i:i+length] == '('+ 'R'*x +')':
                b = b[:i] + b[i+1:i+x+1] + b[i+x+2:]
                cnt += x+1
                i = -1
            i += 1
        x += 1
        length += 1
    print('#{} {}'.format(test_case, cnt))
    '''