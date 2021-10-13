"""
brute-force
"""
def solve(K, L):
    """
    # 서로 경기하나 확인
    :param K: 번호가 작은 선수
    :param L: 번호가 큰 선수
    :return: boolean
    """
    if K%2 and K + 1 == L:
        return True
    return False
def divide(x):
    """
    토너먼트 숫자 //2 함수
    8 -> 4
    9 -> 5 (9//2 로 안됨)
    :param x: 그전 토너먼트 번호
    :return: 라운드 후 토너먼트 번호
    """
    if x%2:
        return x//2 + 1
    else:
        return x//2

def tournament(N, K, L):
    ans = 1
    while N >= 1:
        N = N // 2
        if solve(K, L):
            return ans
        K = divide(K)
        L = divide(L)
        ans += 1
    return -1

N, K, L = map(int, input().split())
if K > L:
    K, L = L, K
print(tournament(N, K, L))