n_str = input()
k = int(input())

dp1 = [[0] * (k + 2) for _ in range(len(n_str) + 1)]
dp2 = [[0] * (k + 2) for _ in range(len(n_str) + 1)]
# dp1[i][j] : 上から i 桁はnと一致していて、0でない数が j 個現れているような数
# dp2[i][j] : 上から i 桁が既にnより小さく、0でない数が j 個現れているような数

# init
dp1[0][0] = 1

for i in range(len(n_str)):
    for j in range(k + 1):
        if n_str[i] != '0':
            # dp1
            dp1[i + 1][j + 1] += dp1[i][j]

            # dp2
            dp2[i + 1][j + 1] += dp1[i][j] * (int(n_str[i]) - 1)
            dp2[i + 1][j + 1] += dp2[i][j] * 9

            dp2[i + 1][j] += dp1[i][j]
            dp2[i + 1][j] += dp2[i][j]
        else:
            # dp1
            dp1[i + 1][j] += dp1[i][j]

            # dp2
            dp2[i + 1][j + 1] += dp2[i][j] * 9

            dp2[i + 1][j] += dp2[i][j]

# print(*dp1, sep='\n')
# print(*dp2, sep='\n')
ans = dp1[len(n_str)][k] + dp2[len(n_str)][k]
print(ans)
