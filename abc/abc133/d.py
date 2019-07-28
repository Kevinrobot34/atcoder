s = input()

dp = [[0 for i in range(13)] for j in range(2)]
if s[i] == '?':
    for i in range(10):
        dp[0][i] = 1
else:
    dp[0][int(s[i])] = 1

print(dp)
# for i in range(1, len(s)):
#
