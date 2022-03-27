N = input()
N_dict = {}
for i in range(9):
    N_dict[str(i)] = 0

for i in N:
    if i in ['6', '9']:
        N_dict['6'] += 1
    else:
        N_dict[i] += 1

if N_dict['6'] % 2:
    N_dict['6'] = N_dict['6'] // 2 + 1
else:
    N_dict['6'] = N_dict['6'] // 2

print(max(N_dict.values()))