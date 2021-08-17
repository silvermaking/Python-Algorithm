def palindrome(lst):
    for i in range(len(lst)//2):
        if lst[i:M+i] == lst[i:M+i][::-1]:
            return lst[i:M+i]
    return None

import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    n_list = [input() for _ in range(N)]
    for i in range(N):
        if palindrome(n_list[i]):
            print(f'#{test_case} {palindrome(n_list[i])}')
            break
        else:
            lst2 = ''
            for j in range(N):
                lst2 += n_list[j][i]

        if palindrome(lst2):
            print(f'#{test_case} {palindrome(lst2)}')
            break
