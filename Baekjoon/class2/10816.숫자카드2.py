import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
c = Counter(N_list)

ans = ' '.join(f'{c[m]}' if c[m] else '0' for m in M_list)
print(ans)
