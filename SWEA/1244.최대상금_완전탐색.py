'''
완전탐색
32847
1. 82347
2. 87342
3 .
87432
완전탐색
# https://ljw538.tistory.com/41
'''
# import sys
# sys.stdin = open('input.txt', "r")
T = int(input())
for tc in range(1, T + 1):
    n, c = input().split()
    c = int(c)
    a = set([n]) #set으로 중복 없애기
    b = set()
    for _ in range(c): #바꾼횟수만큼
        while a:  #모든 경우의 수 고려
            s = a.pop()
            s = list(s)
            for i in range(len(n)):
                for j in range(i+1,len(n)):
                    s[i], s[j] = s[j], s[i]
                    b.add("".join(s))
                    s[i], s[j] = s[j], s[i]
        a, b = b, a

    print(f'#{tc} {max(map(int, a))}')
