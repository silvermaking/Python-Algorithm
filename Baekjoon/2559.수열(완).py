'''
완료
sum을 계속 쓰면 10000번까지 해야해서 시간초과발생
'''
N, K = map(int, input().split()) #N 전체 날짜(2,10001), K연속날짜
temperature = list(map(int, input().split()))

slice_sum = sum(temperature[:K])
lst = [slice_sum]
for i in range(0, N-K):
    slice_sum = slice_sum - temperature[i] + temperature[i+K]
    lst.append(slice_sum)
print(max(lst))