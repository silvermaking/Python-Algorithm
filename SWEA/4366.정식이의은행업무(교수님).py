'''
비트

'''
def change_to_dec(num, notation):
    tmp = 0
    for n, val in enumerate(list(map(int, num))[::-1]):
        tmp += val*(notation**n)
    return tmp

def check(num, notation):
    change_num = change_to_dec(num, notation)
    #change_num = int(num, notation)

    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(notation):
            if val == j: continue
            tmp = change_num - val * (notation ** n) + j * (notation ** n)

            if tmp not in binary:
                binary.append(tmp)
            else:
                return tmp
def check2():
    bi_num = 0
    for x in bi:
        bi_num = bi_num * 2 + int(x)
    for i in rnage(len(bi)):
        binary.append(bi_num ^ (1 << i))

    for i in range(len(tr)):
        num1 = 0
        num2 = 0
        for j in range(len(tr)):
            if i != j:
                num1 = num1 * 3 + int(tr[j])
                num2 = num2 * 3 + int(tr[j])
            else:
                num1 = num1 * 3 + (int(tr[j]) + 1) % 3
                num2 = num2 * 3 + (int(tr[j]) + 1) % 3
        if num1 in binary:
            return num1
        if num2 in binary:
            return num2

for tc in range(1, int(input()) + 1):
    bi = input()
    tr = input()

    binary = []
    check(bi, 2)

    print('#{} {}'.format(tc, check(tr, 3)))