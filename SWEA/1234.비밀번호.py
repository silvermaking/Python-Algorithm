for test_case in range(1, 11):
    N, words = input().split()
    N = int(N)
    ST = []
    for i in range(N):
        if not ST or ST[-1] != words[i]:
            ST.append(words[i])
        elif ST and ST[-1] == words[i]:
            ST.pop()
    answer = ''.join(ST)
    print('#%s %s' %(test_case, answer))
