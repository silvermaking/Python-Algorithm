words = input()
N = len(words)

for i in range(0, N+10, 10):
    print(words[i:i+10])
