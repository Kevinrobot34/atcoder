from collections import defaultdict
n, k = map(int, input().split())

dp = [[1] * (n + 1) for _ in range(2)]

n = 24
d = defaultdict(list)
for i in range(1, n + 1):
    d[n // i].append(i)
for k, v in d.items():
    print(k, v)

n = 36
d = {}
for i in range(1, n):
    if i * i > n:
        break
    d[i] = ((n + i + 1) // (i + 1), n // i)
    print(i, ((n + i + 1) // (i + 1), n // i),
          [n // i for i in range(d[i][0], d[i][1] + 1)])

for i in range(k - 1):
    dp[(i + 1) % 2] = [0] * (n + 1)
    for y in range(1, n + 1):
        for x in range(1, n // y + 1):
            dp[(i + 1) % 2][y] += dp[i % 2][x]

ans = sum(dp[(k - 1) % 2])
print(*dp, sep='\n')
print(ans)
