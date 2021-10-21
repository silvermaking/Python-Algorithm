"""
조합, 재귀
"""
def comb(x, num):
    if x == 6:
        print(*arr)
        return
    for i in range(num, K):
        if used[i]: continue
        used[i] = 1
        arr.append(S[i])
        comb(x+1, i)
        arr.pop()
        used[i] = 0

while True:
    a = input()
    if a == '0':
        break
    lst = list(map(int, a.split()))
    K = lst.pop(0)
    S = lst
    arr = []
    used = [0] * K
    comb(0, 0)
    print()