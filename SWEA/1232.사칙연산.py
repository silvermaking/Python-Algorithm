cal = ['-', '+', '*', '/']
def cal_tree(n):
    if len(tree[n]) > 1:
        if len(tree[int(tree[n][1])]) > 1:
                cal_tree(int(tree[n][1]))
                left = stack.pop()
        else:
            left = int(tree[int(tree[n][1])][0])

        if len(tree[int(tree[n][2])]) > 1:
                cal_tree(int(tree[n][2]))
                right = stack.pop()
        else:
            right = int(tree[int(tree[n][2])][0])

    if tree[n][0] == cal[0]:
        stack.append(left - right)
    elif tree[n][0] == cal[1]:
        stack.append(left + right)
    elif tree[n][0] == cal[2]:
        stack.append(left * right)
    elif tree[n][0] == cal[3]:
        stack.append(left / right)

for tc in range(1,11):
    N = int(input())
    tree = [0]
    for _ in range(N):
        tree.append(input().split()[1:])
    stack = []
    cal_tree(1)
    ans = stack.pop()
    ans = round(ans)
    print(f'#{tc} {ans}')
