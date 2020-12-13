s = input()
t = input()

n, m = len(s), len(t)

dp1 = [[0] * (m + 1) for _ in range(n + 1)]
# dp1[i][j] = (a[:i], b[:j]まで見たときのLCS(Longest Common Subsequence))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        c1 = dp1[i - 1][j - 1] + int(s[i - 1] == t[j - 1])
        c2 = dp1[i - 1][j]
        c3 = dp1[i][j - 1]
        dp1[i][j] = max(c1, c2, c3)

print(dp1[n][m])
