import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
graph_dim_out = [0] * n
for i in range(m):
    s, t = map(int, input().split())
    s, t = s - 1, t - 1
    graph_dim_out[s] += 1
    graph[s].append(t)


def func(x):
    dp = [0] * n
    for i in reversed(range(n - 1)):
        if i != x or graph_dim_out[x] == 1:
            for j in graph[i]:
                dp[i] += dp[j]
            dp[i] = dp[i] / graph_dim_out[i] + 1
        else:
            k = -1
            for j in graph[i]:
                dp[i] += dp[j]
                if k == -1 or dp[k] < dp[j]:
                    k = j
            dp[i] -= dp[k]
            dp[i] = dp[i] / (graph_dim_out[i] - 1) + 1

    return dp[0]


ans = func(0)
for x in range(1, n - 1):
    ans = min(ans, func(x))

print(ans)
