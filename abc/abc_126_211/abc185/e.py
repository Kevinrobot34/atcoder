n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp1 = [[0] * (m + 1) for _ in range(n + 1)]
# dp1[i][j] = (a[:i], b[:j]まで見たときのLCS(Longest Common Subsequence))
dp2 = [[(0, 0)] * (m + 1) for _ in range(n + 1)]

ans = max(n, m)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp1[i][j] = dp1[i - 1][j - 1] + 1
            if dp1[i][j] == 1:
                dp2[i][j] = (i, j)
            else:
                dp2[i][j] = dp2[i - 1][j - 1]

            i0, j0 = dp2[n][m]
            z = min(i0, j0) + min(i - i0, j - j0) + min(n - i, m - j)
            z = min(z, min(n, m))
            x = n + m - z * 2
            y = z - dp1[i][j]
            ans = min(ans, x + y)
        else:
            dp1[i][j] = max(dp1[i - 1][j], dp1[i][j - 1])
            if dp1[i - 1][j] > dp1[i][j - 1]:
                dp2[i][j] = dp2[i - 1][j]
            else:
                dp2[i][j] = dp2[i][j - 1]

dp1 = [[0] * (m + 1) for _ in range(n + 1)]
# dp1[i][j] = (a[:i], b[:j]まで見たときのLCS(Longest Common Subsequence))
dp2 = [[(0, 0)] * (m + 1) for _ in range(n + 1)]
for j in range(1, m + 1):
    for i in range(1, n + 1):
        if a[i - 1] == b[j - 1]:
            dp1[i][j] = dp1[i - 1][j - 1] + 1
            if dp1[i][j] == 1:
                dp2[i][j] = (i, j)
            else:
                dp2[i][j] = dp2[i - 1][j - 1]

            i0, j0 = dp2[n][m]
            z = min(i0, j0) + min(i - i0, j - j0) + min(n - i, m - j)
            z = min(z, min(n, m))
            x = n + m - z * 2
            y = z - dp1[i][j]
            ans = min(ans, x + y)
        else:
            dp1[i][j] = max(dp1[i - 1][j], dp1[i][j - 1])
            if dp1[i - 1][j] > dp1[i][j - 1]:
                dp2[i][j] = dp2[i - 1][j]
            else:
                dp2[i][j] = dp2[i][j - 1]

# print(*dp1, sep='\n')
# print(*dp2, sep='\n')
print(ans)
