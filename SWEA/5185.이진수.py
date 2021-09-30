hex_dict = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9,
        'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}

def hextodec(x):
    global result
    for i in range(4):
        a = x // 2
        b = x % 2
        result = str(b) + result
        x = a
    return

for tc in range(1, int(input()) + 1):
    N, x = input().split()
    answer = ''
    for i in x:
        result = ''
        hextodec(hex_dict[i])
        answer += result
    print(f'#{tc} {answer}')