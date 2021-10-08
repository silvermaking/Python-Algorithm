'''
기초적 greedy 문제
----------------
큰 동전부터 차례대로 탐욕적으로 선택하기
'''

coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, int(input()) + 1):
    N = int(input())
    cnt = []
    for coin in coins:
        cnt.append(str(N // coin)) # 출력을 위해 문자열로 append
        N %= coin
    print('#' + str(tc))
    print(*cnt)