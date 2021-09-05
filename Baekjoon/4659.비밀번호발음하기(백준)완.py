vowels = ['a', 'e', 'i', 'o', 'u']
def IsAccept(password):
    # 1. 모음 적어도 하나
    cnt = 0
    # 2. 모음 자음 3개 연속x
    cnt_a = 0
    cnt_b = 0
    for p in password:
        if p in vowels:
            cnt = 1
            cnt_a += 1
            cnt_b = 0
        else:
            cnt_a = 0
            cnt_b += 1
        if cnt == 0:
            return f'<{password}> is not acceptable.'
        if cnt_a == 3 or cnt_b == 3:
            return f'<{password}> is not acceptable.'
    # 3. 같은 글자 연속 x
    for i in range(1, N):
        if password[i-1] == password[i] and password[i - 1:i + 1] not in ['ee', 'oo']:
            return f'<{password}> is not acceptable.'

    return f'<{password}> is acceptable.'

while True:
    password = input()
    N = len(password)
    if password == 'end':
        break
    print(IsAccept(password))