#DP
# ARR = [0] * 31
# ARR[1] = 1
# ARR[2] = 3
# for n in range(3, 31):
#     ARR[n] = ARR[n-1] + 2 * ARR[n-2]

#점화식
def DP(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return DP(n-1) + 2*DP(n-2)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case} {DP(N//10)}')