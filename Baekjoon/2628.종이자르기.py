#https://www.acmicpc.net/problem/2628
Y, X = map(int, input().split()) #가로, 세로
N = int(input())
answer = [] # 넓이 append
X_list = [X]
Y_list = [Y]
for i in range(N):
    a, b = map(int, input().split())
    if a == 0: #가로
        X_list.append(b)
    else:
        Y_list.append(b)

X_list.sort()
NewX_list = [X_list[0]]
Y_list.sort()
NewY_list = [Y_list[0]]

for i in range(1, len(X_list)):
    NewX_list.append(X_list[i] - X_list[i-1])
for i in range(1, len(Y_list)):
    NewY_list.append(Y_list[i] - Y_list[i-1])

for x in NewX_list:
    for y in NewY_list:
        answer.append(x*y)

print(max(answer))

