a = '3+4+5*6*7+7'
'''
34+56*7*+7+
7  30 
    217 7
'''
def step(s):
    isp = {'*' : 2, '+' : 1, '(' : 3, ')' : 0}
    t = []
    ST = []
    for c in s:
        if c.isdecimal():
            t.append(c)
        else:
            # 연산자의 우선순위에 의한 작업
            if len(ST)==0 or isp[ST[-1]]<isp[c] or c == '(':
                ST.append(c)
            else:
                if c == '+':
                    while ST and isp[ST[-1]] >= isp[c]:
                        if ST[-1] == '(':
                            ST.append(c)
                            break
                        else:
                            t.append(ST.pop())
                elif c == '*':
                    if ST[-1] == '(':
                        ST.append(c)
                    else:
                        t.append(ST.pop())
                        ST.append(c)

                elif c == ')':  #')'
                    while ST and ST[-1] != '(':
                        t.append(ST.pop())
                    ST.pop()
    while ST:
        t.append(ST.pop(-1))
    return t

def step2(t):
    ST = []
    for c in t:
        if c.isdecimal():
            ST.append(int(c))
        else:
            # 연산자의 우선순위에 의한 작업
            n1 = int(ST.pop())
            n2 = int(ST.pop())
            if c == '+':
                ST.append(n1+n2)
            if c == '*':
                ST.append(n1*n2)
    return sum(ST)

for test_case in range(1,11):
    N = int(input())
    s = input()
    t = step(s)
    answer = step2(t)
    print('#{} {}'.format(test_case, answer))