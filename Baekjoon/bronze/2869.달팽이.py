A, B, V = map(int, input().split())
ans = (V - A - 1) // (A - B) + 2
print(ans)
