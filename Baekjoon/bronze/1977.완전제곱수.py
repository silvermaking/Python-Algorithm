M = int(input())
N = int(input())
ans = []
nums = [i for i in range(int(M ** 0.5),int(N ** 0.5) + 1)]
for i in range(M, N+1):
    if (i ** 0.5) in nums:
        ans.append(i)

if ans:
    print(sum(ans), min(ans), sep='\n')
else:
    print(-1)