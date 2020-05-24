import sys
sys.setrecursionlimit(10**9)

t = int(input())
for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    memo = {0: n * d}

    def dfs(m, cost):
        if m not in memo or memo[m] > cost:
            memo[m] = cost
            memo[0] = min(memo[0], cost + m * d)

            if m > 0:
                dfs(m // 2, cost + (m % 2) * d + a)
                dfs(m // 3, cost + (m % 3) * d + b)
                dfs(m // 5, cost + (m % 5) * d + c)

                dfs((m + (2 - m % 2) % 2) // 2, cost + (2 - m % 2) % 2 * d + a)
                dfs((m + (3 - m % 3) % 3) // 3, cost + (3 - m % 3) % 3 * d + b)
                dfs((m + (5 - m % 5) % 5) // 5, cost + (5 - m % 5) % 5 * d + c)

    dfs(n, 0)
    print(memo[0])
