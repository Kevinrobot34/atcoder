import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = True
    graph[b][a] = True


def check_comp(bit):
    targets = [i for i in range(n) if (bit >> i) & 1]
    for i in range(len(targets)):
        for j in range(i):
            if not graph[targets[i]][targets[j]]:
                return False
    return True


dp = [n] * (1 << n)
dp[0] = 0
for bit in range(1 << n):
    if check_comp(bit):
        dp[bit] = 1

for s in range(1 << n):
    t = s
    while t > 0:
        dp[s] = min(dp[s], dp[t] + dp[s - t])
        t = (t - 1) & s

print(dp[(1 << n) - 1])
