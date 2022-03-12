def solve(x, s):
    if x == M:
        print(*arr)
        return

    for i in range(s, N + 1):
        if used[i]: continue
        arr.append(i)
        used[i] = 1
        solve(x + 1, i)
        used[i] = 0
        arr.pop()


N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]
arr = []
used = [0] * (N + 1)
solve(0, 1)