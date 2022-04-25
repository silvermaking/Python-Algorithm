def isVPS(words):
    st = []
    for word in words:
        if word == '(':
            st.append(word)
        else:
            if st and st[-1] == '(':
                st.pop()
            else:
                return False
    if st:
        return False
    else:
        return True

for _ in range(int(input())):
    xs = input()
    if isVPS(xs):
        print('YES')
    else:
        print('NO')
