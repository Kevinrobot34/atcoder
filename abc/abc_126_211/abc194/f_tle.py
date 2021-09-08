MOD = 10**9 + 7
n, k = input().split()
k = int(k)
d = 16
m = 1 << d
l = len(n)

dp1 = [[0] * m for _ in range(l + 1)]
dp2 = [[0] * m for _ in range(l + 1)]
# dp1[i][j] : (16進数で)上から i 桁はnと一致していて、使われている数字の集合がjであるような数
# dp2[i][j] : (16進数で)上から i 桁が既にnより小さく、使われている数字の集合がjであるような数

dp1[0][0] = 1
for i in range(l):
    ni = int(n[i], d)

    for j in range(m):
        if dp1[i][j] == 0 and dp2[i][j] == 0:
            continue

        # 1 -> 1
        j_11 = j | (1 << ni)
        dp1[i + 1][j_11] += dp1[i][j]
        dp1[i + 1][j_11] %= MOD

        for x in range(d):
            j2 = j if j == 0 and x == 0 else j | (1 << x)

            if x < ni:
                # 1 -> 2
                dp2[i + 1][j2] += dp1[i][j]
                dp2[i + 1][j2] %= MOD

            # 2 -> 2
            dp2[i + 1][j2] += dp2[i][j]
            dp2[i + 1][j2] %= MOD

ans = 0
for j in range(m):
    if bin(j).count('1') == k:
        ans += dp1[l][j] + dp2[l][j]
        ans %= MOD
print(ans)
