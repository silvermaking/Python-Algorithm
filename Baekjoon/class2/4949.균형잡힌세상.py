def isWords(words):
    stack = []
    if words == '.':
        return
    for word in words:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')':
            if not stack or stack[-1] == '[':
                print('no')
                return
            elif stack[-1] == '(':
                stack.pop()

        elif word == ']':
            if not stack or stack[-1] == '(':
                print('no')
                return
            elif stack[-1] == '[':
                stack.pop()

    if len(stack): # ( or [ 만 가득차있을때 방지
        print('no')
    else:
        print('yes')
    return

while True:
    x = input()
    if x == '.':
        break
    stack = []
    isWords(x)