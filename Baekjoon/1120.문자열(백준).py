'''
구현, 문자열
길이: A <= B

'''
import sys
A, B = sys.stdin.readline().split()

# 원래 길이가 같으면
if len(A) == len(B):
    cnt = 0
    for i in range(len(B)):
        if A[i] != B[i]:
            cnt += 1

else:
    # A를 움직여가며 B와 가장 많이 같을 때 찾기
    # == cnt 가 가장 최소일 때
    cnt = len(A)
    for i in range(len(B)-len(A)+ 1):
        temp_cnt = 0
        temp_B = B[i:i+len(A)]
        for i in range(len(A)):
            if temp_B[i] != A[i]:
                temp_cnt += 1
        if cnt > temp_cnt:
            cnt = temp_cnt

        if cnt == 0:
            break
print(cnt)