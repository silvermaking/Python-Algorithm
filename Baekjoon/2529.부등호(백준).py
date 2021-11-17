"""
완전탐색
backtracking
"""
def solve(x, ans):
    global min_ans, max_ans
    if x == K+1:
        if int(ans) < min_ans:
            min_ans = int(ans)
        if int(ans) > max_ans:
            max_ans = int(ans)
        return

    for i in range(len(nums)):
        if visited[i]: continue
        if x:
            if lst[x-1] == ">":
                if int(ans[x-1]) <= nums[i]: continue

            else:
                if int(ans[x-1]) >= nums[i]: continue

        visited[i] = 1
        solve(x + 1, ans + str(nums[i]))
        visited[i] = 0

nums = [i for i in range(0, 10)]
visited = [0] * 10
K = int(input())
lst = list(input().split())
min_ans = 9999999999
max_ans = 0

solve(0, "")
min_ans = str(min_ans)
while len(min_ans) < K+1:
    min_ans = "0" + min_ans
print(max_ans, min_ans, sep='\n')
