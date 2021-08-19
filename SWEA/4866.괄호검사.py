import sys
sys.stdin = open('sample_input (2).txt', 'r')
'''
{ ( } )  : 짝이 안맞는 경우 고려
'''
T = int(input())
for test_case in range(1, T+1):
    sentence = input()
    ST = []
    for word in sentence:
        if word == '{':
            ST.append(word)
        elif word == '(':
            ST.append(word)
        elif word == '}':
            if '{' in ST and ST[-1] == '{':
                ST.pop(-1)
            else:
                ST.append(1)
                break
        elif word == ')':
            if '(' in ST and ST[-1] == '(':
                ST.pop(-1)
            else:
                ST.append(1)
                break

    if len(ST):
        print(f'#{test_case} {0}')
    else:
        print(f'#{test_case} {1}')