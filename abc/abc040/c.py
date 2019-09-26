n = int(input())
a = list(map(int, input().split()))

INF = float('inf')
cost = [INF] * n
cost[0] = 0
for i in range(n):
    if i + 1 < n:
        cost[i+1] = min(cost[i+1], cost[i] + abs(a[i+1] - a[i]))
    if i + 2 < n:
        cost[i+2] = min(cost[i+2], cost[i] + abs(a[i+2] - a[i]))

print(cost[-1])
