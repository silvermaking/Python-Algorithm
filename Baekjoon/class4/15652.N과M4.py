def solve(x, s):
    if x == M:
        print(*arr)
        return

    for i in range(s, N + 1):
        arr.append(i)
        solve(x + 1, i)
        arr.pop()


N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
arr = []
solve(0, 1)