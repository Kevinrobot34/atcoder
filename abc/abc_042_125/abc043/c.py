n = int(input())
a = list(map(int, input().split()))

a_min = min(a)
a_max = max(a)

ans = 200**2 * 105
for b in range(a_min, a_max+1):
    cost = 0
    for i in range(n):
        cost += (a[i] - b) ** 2
    ans = min(ans, cost)

print(ans)
