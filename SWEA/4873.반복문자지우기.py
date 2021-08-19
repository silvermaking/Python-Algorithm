import sys
sys.stdin = open('sample_input (3).txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    words = input()
    lst = []
    for word in words:
        lst.append(word)
    i = -1
    while i < len(lst)-2:
        i += 1
        if lst[i] == lst[i+1]:
            lst.pop(i)
            lst.pop(i)
            i = -1
    print('#{} {}'.format(test_case, len(lst)))
