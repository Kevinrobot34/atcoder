n = int(input())
x = tuple(map(int, input().split()))

ans = 100**3
for p in range(1, 101):
    cost = sum((xi - p)**2 for xi in x)
    ans = min(ans, cost)

print(ans)
