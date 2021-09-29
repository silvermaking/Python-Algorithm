# 홀수자리의합 x3 + 짝수자리의 합 + 검증 코드 = 10
def IsOne(passwords):
    for j in range(N):
        for i in range(M-1, -1, -1):
            if passwords[j][i] == '1':
                return j, i
pass_solve = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
for tc in range(1, int(input()) + 1):
    # N : 세로, M : 가로
    N, M = map(int, input().split())
    passwords = [input() for _ in range(N)]
    j, pos = IsOne(passwords)
    #실제 암호 56자리
    code = passwords[j][pos-55:pos+1]
    check = [0]
    for i in range(0, 56, 7):
        check.append(pass_solve[code[i:i+7]])

    a = check[1] + check[3] + check[5] + check[7]
    b = a * 3 + check[2] + check[4] + check[6] + check[8]
    answer = 0
    if b%10 == 0:
        answer = sum(check)

    print(f'#{tc} {answer}')