"""
brute-force
"""

import sys
input = sys.stdin.readline

def solve(cnt, lst):
    global ans
    if len(lst) == 2:
        if cnt > ans:
            ans = cnt
            return

    for i in range(1, len(lst)-1):
        temp_cnt = lst[i-1] * lst[i+1]
        temp = lst[i]
        del lst[i]

        solve(cnt + temp_cnt, lst)
        lst.insert(i, temp)

N = int(input())
lst = list(map(int, input().strip().split()))
ans = 0
solve(0, lst)
print(ans)