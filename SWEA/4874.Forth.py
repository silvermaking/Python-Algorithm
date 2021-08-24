import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for test_case in range(1, T+1):
    Forth = list(input().split())
    ST = []
    for s in Forth:
        if s.isdecimal():
            ST.append(s)
        else:
            if s == '.':
                if len(ST) == 1:
                    answer = ST.pop()
                    print(f"#{test_case} {answer}")
                    break
                else:
                    print(f"#{test_case} error")
                    break
            if len(ST) < 2:
                print(f"#{test_case} error")
                break
            if s == '+':
                a = int(ST.pop())
                b = int(ST.pop())
                ST.append(a+b)
            elif s == '-':
                a = int(ST.pop())
                b = int(ST.pop())
                ST.append(b-a)
            elif s == '*':
                a = int(ST.pop())
                b = int(ST.pop())
                ST.append(a*b)
            elif s == '/':
                a = int(ST.pop())
                b = int(ST.pop())
                ST.append(b//a)


