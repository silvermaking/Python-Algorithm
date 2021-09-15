def groupword(lst):
    ST =[lst[0]]  #[a]
    if len(lst) == 1:
        return 1
    for s in lst:
        if ST[-1] != s:
            ST.append(s)

        if s in ST[:-1]:
            return 0
    return 1

N = int(input())
a_lst = [input() for _ in range(N)]
cnt = 0
for a in a_lst:
    cnt += groupword(a)
print(cnt)
