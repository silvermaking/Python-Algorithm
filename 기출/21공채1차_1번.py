id_dict = {}

id_list = ["con", "ryan"]
for id in id_list:
    id_dict[id] = 0

re_list = [[] for _ in range(len(id_list))]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
'''
input들
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
- 동일한 유저 계속 신고 x
'''
def findRe(str):
    i = 0
    while True:
        if str[i] == ' ':
            break
        i += 1
    id1 = str[:i]
    id2 = str[i+1:]
    return id1, id2

for re in report:
    id1, id2 = findRe(re)
    if id2 not in re_list[id_list.index(id1)]:
        re_list[id_list.index(id1)].append(id2)
        id_dict[id2] += 1

answer = [0] * len(id_list)
for key, value in id_dict.items():
    if value >= k:
        for i in range(len(re_list)):
            if key in re_list[i]:
                answer[i] += 1

print(answer)