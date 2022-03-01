import sys

word_list = list(sys.stdin.readline().strip())
for i in range(97, 123):
    temp = chr(i)
    if temp not in word_list:
        print(-1, end=' ')
    else:
        print(word_list.index(temp), end=' ')