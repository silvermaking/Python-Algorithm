import sys
sys.stdin = open('input1244.txt', "r")

def solve(k):
    global maxV
    if k == N:
        intV = int("".join(pan))
        if maxV < intV:
            maxV = intV
        return

    intV = int("".join(pan))
    for i in range(720):
        if state[k][i] == intV:
            return
        if state[k][i] == 0:
            state[k][i] = intV
            break

    L = len(pan)
    for i in range(0, L-1):
        for j in range(i+1, L):
            pan[i], pan[j] = pan[j], pan[i]
            solve(k+1)
            pan[i], pan[j] = pan[j], pan[i]

T = int(input())
# T = 4
for tc in range(1, T + 1):
    pan, N = input().split()
    pan = list(pan)
    N = int(N)
    state = [[0] * 720 for _ in range(N)]     #[k][6!]
    maxV = 0
    solve(0)
    print(maxV)
