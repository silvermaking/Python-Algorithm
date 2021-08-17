import sys
sys.stdin = open('sample_input.txt', 'r')

def match(a,b):
    for i in range(len(b)-len(a)+1):
        for j in range(len(a)):
            if b[i+j] != a[j]:
                break
        else:
            return 1
    return 0
''' 
보이어무어 알고리즘이 시간초과가 된다...
def BM(P, T):
    M = len(P)
    N = len(T)

    SKIP = [M] * 128  # 아스키코드는 제어문자 제외 7bit 사용(32~126)
    for i in range(M):
        pos = ord(P[i])
        SKIP[pos] = M-i-1

    idxT = 0 #시작위치
    while idxT <= N-M:
        idxP = M-1 #끝위치
        while idxP >= 0 and T[idxT + idxP] == P[idxP]:
            idxP -= 1
        if idxP == -1:
            return 1
        idxT = idxT + SKIP[ord(T[idxT+M-1])]

    return 0
    '''

T = int(input())
for test_case in range(1, T+1):
    P = input()
    T = input()
    print('#{} {}'.format(test_case, match(P, T)))