import sys

max_num = 0
max_idx = 0
for i in range(1, 10):
    num = int(sys.stdin.readline())
    if num > max_num:
        max_num = num
        max_idx = i

print(max_num, max_idx, sep='\n')