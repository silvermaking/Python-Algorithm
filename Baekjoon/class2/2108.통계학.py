from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

# 1. 산술평균
avg = round(sum(lst) / N)
print(avg)
# 2. 중앙값
lst2 = sorted(lst)
print(lst2[N//2])

# 3. 최빈값
lst2_c = Counter(lst2).most_common()
if len(lst2_c) > 1:
    if lst2_c[0][1] == lst2_c[1][1]:
        print(lst2_c[1][0])
    else:
        print(lst2_c[0][0])
else:
    print(lst2_c[0][0])

# 4
print(lst2[-1] - lst2[0])