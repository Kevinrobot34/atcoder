n, m = map(int, input().split())
edge = [[0] * n for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edge[y][x] = 1

N_STATE = 1 << n
dp = [0] * N_STATE
dp[0] = 1
for bit in range(N_STATE):
    for i in range(n):
        if (bit >> i) & 1 == 1:
            continue
        is_possible = True
        for j in range(n):
            if (bit >> j) & 1 == 1 and edge[j][i] == 1:
                is_possible = False
                break
        if is_possible:
            dp[bit | (1 << i)] += dp[bit]

# print(dp)
print(dp[-1])
