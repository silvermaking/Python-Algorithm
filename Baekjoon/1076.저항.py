values = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
          'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
          'grey': 8, 'white': 9}
multiples = {'black': 1, 'brown': 10, 'red': 100, 'orange': 1000,
          'yellow': 10000, 'green': 100000, 'blue': 1000000, 'violet': 10000000,
          'grey': 100000000, 'white': 1000000000}

colors = [input() for _ in range(3)]
ans = ''
for i in range(3):
    if i >= 2:
        temp = multiples[colors[i]]
        ans = int(ans) * temp
    else:
        ans += str(values[colors[i]])

print(ans)