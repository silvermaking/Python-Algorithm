import sys

num_dict = {}
for i in range(10):
    num_dict[str(i)] = 0

number = 1
for _ in range(3):
    temp = int(sys.stdin.readline())
    number *= temp

for i in str(number):
    num_dict[i] += 1

for value in num_dict.values():
    print(value)
