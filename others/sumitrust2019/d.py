n = int(input())
s = input()

dp = [set(), set()]

dp[0].add("")
for i in range(n):
    dp[(i + 1) % 2] = dp[i % 2].copy()
    i1 = (i + 1) % 2
    i0 = (i + 0) % 2
    for j in dp[i0]:
        if len(j) < 3:
            dp[i1].add(j + s[i])

ans = 0
for j in dp[n % 2]:
    if len(j) == 3:
        # print(j)
        ans += 1

print(ans)
