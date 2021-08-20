import sys
sys.stdin = open('s_input.txt', "r")
T = int(input())
for test_case in range(1, T+1):
    a = input()
    # (()())
    stack = []
    ans = 0
    for i in range(len(a)):
        if a[i] == '(':  # 막대수 누적
            stack.append('(')
        else:
            stack.pop()
            if a[i-1] =='(': #레이저 지나면 누적값 더하기
                ans += len(stack)
            else:  # 막대 끝나면 누적값-1 ans값 +1
                ans += 1
    print('#{} {}'.format(test_case, ans))
