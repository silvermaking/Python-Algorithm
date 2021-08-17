def typing(A, B):
    i = 0
    cnt = 0
    while i < len(A):
        if A[i:i+len(B)] == B:
            i += len(B)
        else:
            i += 1
        cnt += 1
    return cnt
T = int(input())
for test_case in range(1, T+1):
    A, B = input().split()
    print('#{} {}'.format(test_case, typing(A, B)))