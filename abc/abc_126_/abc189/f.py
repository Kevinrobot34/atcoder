n, m, k = map(int, input().split())
a = set(map(int, input().split()))

dp1 = [0] * (n + 1)
dp2 = [0] * (n + 1)

dp1_cs = [0] * (n + 1)  # dp1_cs[i] = sum(dp1[i:])
dp2_cs = [0] * (n + 1)  # dp2_cs[i] = sum(dp2[i:])

for i in reversed(range(n)):
    l = i + 1
    r = min(n, i + m + 1)

    if i in a:
        dp1[i] = 1.0
    else:
        dp1[i] = (dp1_cs[l] - dp1_cs[r]) / m
        dp2[i] = (dp2_cs[l] - dp2_cs[r]) / m + 1.0

    dp1_cs[i] = dp1_cs[i + 1] + dp1[i]
    dp2_cs[i] = dp2_cs[i + 1] + dp2[i]

if dp1[0] == 1.0:
    ans = -1
else:
    ans = dp2[0] / (1.0 - dp1[0])
print(ans)
