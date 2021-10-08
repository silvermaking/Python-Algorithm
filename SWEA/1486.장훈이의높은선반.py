'''
부분집합
powerset 재귀 이용

'''
def powerset(idx, s):
    global min_s
    if B <= s < min_s:
        min_s = s
    if idx == N:
        return
    powerset(idx+1, s)
    powerset(idx+1, s + lst[idx])

for tc in range(1, int(input()) + 1):
    #N : 명, B : 선반의 높이
    N, B = map(int, input().split())
    #N명의 점원 키
    lst = list(map(int, input().split()))
    min_s = 200000
    powerset(0, 0)
    print(f'#{tc} {min_s - B}')