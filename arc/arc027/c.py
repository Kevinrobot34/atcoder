import sys
input = sys.stdin.readline

x, y = map(int, input().split())
n = int(input())
th = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * (x + 1) for _ in range(x + y + 1)] for _ in range(2)]
# dp[i][j][k] = (トッピングiまでで、j枚のチケットでk個のトッピングを入手した時の嬉しさの最大値)

for i, (ti, hi) in enumerate(th):
    i0 = (i + 0) % 2
    i1 = (i + 1) % 2
    for j in range(x + y + 1):
        for k in range(x + 1):
            if j >= ti and k >= 1:
                dp[i1][j][k] = max(dp[i0][j][k], dp[i0][j - ti][k - 1] + hi)
            else:
                dp[i1][j][k] = dp[i0][j][k]

ans = max(max(dp_i) for dp_i in dp[n % 2])
# print(*dp[n % 2], sep='\n')
print(ans)
