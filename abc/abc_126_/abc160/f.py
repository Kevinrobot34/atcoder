import sys
sys.setrecursionlimit(10**9)

MOD = 10**9 + 7
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dp = {}


def f(s):
    ts = tuple(s)
    if ts in dp:
        return dp[ts]
    if len(s) == n - 1:
        return 1

    ans = 0
    for si in s:
        for j in g[si]:
            if j in s:
                continue

            ans += f(s | {j})
            ans %= MOD
    dp[ts] = ans
    return ans


for i in range(n):
    print(f({i}))
