import sys
input = sys.stdin.readline

N = int(input())
cor_list = [list(map(int, input().split())) for _ in range(N)]
cor_list.sort(key=lambda x: (x[0], x[1]))
for cor in cor_list:
    print(*cor)
