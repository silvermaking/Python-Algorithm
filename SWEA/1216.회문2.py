def palindrome(lst):
    for j in range(100, 0, -1):
        for i in range(101-j):
            if lst[i:j+i] == lst[i:j+i][::-1]:
                return j
    return 0

import sys
sys.stdin = open('input.txt', 'r')
for test_case in range(1, 11):
    tc = int(input())
    n_list = [input() for _ in range(100)]
    length = 0
    for i in range(100):
        if palindrome(n_list[i]) > length:
            length = palindrome(n_list[i])

        lst2 = ''
        for j in range(100):
            lst2 += n_list[j][i]

        if palindrome(lst2) > length:
            length = palindrome(lst2)
    print('#{} {}'.format(tc, length))
