burger = []
beverage = []

for _ in range(3):
    burger.append(int(input()))

for _ in range(2):
    beverage.append(int(input()))

ans = min(burger) + min(beverage)
print(ans - 50)