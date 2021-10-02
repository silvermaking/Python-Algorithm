'''
구현으로 풀어보기
32847
1. 82347
2. 87342
3 .
87432
# https://ljw538.tistory.com/41
'''
import sys
sys.stdin = open('input.txt', "r")
for tc in range(1, int(input()) + 1):
    n, c = input().split()
    n_lst = list(n)
    c = int(c)
    final_n = sorted(n_lst, reverse=True)
    while c> 0:
        if n_lst == final_n:
            break
        for i in range(len(n_lst)):
            if n_lst[i] != final_n[i]:
                pos1 = i
                break
        for j in range(len(n_lst)-1, -1, -1):
        # for j in range(len(n_lst)):
            if n_lst[pos1] == final_n[j] and final_n[pos1] == n_lst[j]:
                n_lst[pos1], n_lst[j] = n_lst[j], n_lst[pos1]
                break
        else:
            for k in range(len(n_lst) - 1, -1, -1):
                if n_lst[k] == final_n[pos1]:
                    n_lst[pos1], n_lst[k] = n_lst[k], n_lst[pos1]
                    break
        c -= 1
    if c == 0:
        answer = n_lst
    else:
        if c%2:
            cnt_dict = {}
            for i in final_n:
                try:
                    cnt_dict[i] += 1
                except:
                    cnt_dict[i] = 1
            for key in cnt_dict.keys():
                if cnt_dict[key] > 1:
                    break
            else:
                final_n[-1], final_n[-2] = final_n[-2], final_n[-1]

        answer = final_n

    print(f'#{tc} {"".join(answer)}')
