n, m = map(int, input().split())

drink = []
for i in range(n):
    a, b = map(int, input().split())
    drink.append((a, b))

drink.sort(reverse=True)

ans = 0
while m > 0:
    a, b = drink.pop()
    if m > b:
        ans += a * b
        m -= b
    else:
        ans += a * m
        m = 0

print(ans)
