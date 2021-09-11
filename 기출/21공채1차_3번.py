'''fees = [180, 5000, 10, 600]
#       기본시간, 기본요금, 단위시간(분), 단위요금(원)
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
           "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]'''
import math
re_dict = {}
for record in records:
    t, car = record[:5], record[6:10]
    car = int(car)
    try:
        re_dict[car].append(t)
    except:
        re_dict[car] = [t]
for value in re_dict.values():
    if len(value) % 2:
        value.append('23:59')

re_lst = sorted(re_dict.items())
lst = []
for i in range(len(re_lst)):
    a, b = re_lst[i]
    lst.append(b)

print(lst)
answer = []
ans = 0
for c in lst:
    for j in range(0, len(c), 2):
        h1, m1 = int(c[j][:2]), int(c[j][3:])
        h2, m2 = int(c[j+1][:2]), int(c[j+1][3:])
        if m2 < m1:
            ans += (h2-h1-1)*60 + (m2+60-m1)
        else:
            ans += (h2-h1)*60 + (m2-m1)
    answer.append(ans)
    ans = 0

for i in range(len(answer)):
    if answer[i] > fees[0]:
        f = fees[1] + math.ceil((answer[i]-fees[0])/fees[2])*fees[3]
        print(f)
        answer[i] = f
    else:
        answer[i] = fees[1]
