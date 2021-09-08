n = int(input())

dp1 = [0] * (n + 1)  # true
dp2 = [0] * (n + 1)  # fale
dp1[0] = dp2[0] = 1

for i in range(n):
    si = input()
    if si == 'AND':
        dp1[i + 1] = dp1[i]
        dp2[i + 1] = dp1[i] + dp2[i] * 2
    else:
        dp1[i + 1] = dp1[i] * 2 + dp2[i]
        dp2[i + 1] = dp2[i]

print(dp1[n])
