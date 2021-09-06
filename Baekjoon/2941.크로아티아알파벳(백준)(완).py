C_text = input()

change_c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in change_c:
    C_text = C_text.replace(c, '1')

print(len(C_text))
