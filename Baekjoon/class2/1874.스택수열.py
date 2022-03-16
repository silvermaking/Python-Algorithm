"""
1. 오름차순 stack이므로 반드시 첫 수 만날 때 까지 append,  +
2. 해당하는 수 만나면 pop,  -

print('\n'.join(ans_list) 로 for문 출력 가능
    - 시간복잡도 다소 줄임
"""
import sys

input = sys.stdin.readline

N = int(input())
number_list = [int(input()) for _ in range(N)]
ans_list = []
stack = []
is_true = True
v = 1
for number in number_list:
    while v <= number:
        stack.append(v)
        ans_list.append("+")
        v += 1

    if stack[-1] == number:
        stack.pop()
        ans_list.append("-")
    else:
        print("NO")
        is_true = False
        break

if is_true:
    # for ans in ans_list:
    #     print(ans)
    print('\n'.join(ans_list))