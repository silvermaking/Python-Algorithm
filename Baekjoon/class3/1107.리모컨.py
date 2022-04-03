"""
<brute-force> / 완탐
1. 단순히 +/- 로 세기
2. 모든 버튼에 대해 min값 찾기
"""

def find(num):
    global min_cnt, N, bttns

    for btn in bttns:
        temp = num + str(btn)
        min_cnt = min(min_cnt, abs(N - int(temp)) + len(temp))

        if len(temp) < 6:
            find(temp)

min_cnt = 10e9
N = int(input())
M = int(input())
min_cnt = min(min_cnt, abs(100 - N))
bttns = {i for i in range(10)}
bttns -= set(map(int, input().split())) if M else set()
find('') if M < 10 and min_cnt > 0 else ''
print(min_cnt)


