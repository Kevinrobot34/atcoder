a, b = map(int, input().split())


def calc(x):
    ans = 0
    x_str = str(x)
    digits = len(x_str)

    dp = [[0] * 2 for _ in range(digits + 1)]
    dp[0][0] = 1
    for i in range(digits):
        xi = ord(x_str[i]) - ord('0')
        for d in range(xi + 1):
            if d == 4 or d == 9:
                continue

            if d == xi:
                dp[i + 1][0] += dp[i][0]
            else:
                dp[i + 1][1] += dp[i][0]

        for d in range(10):
            if d == 4 or d == 9:
                continue
            dp[i + 1][1] += dp[i][1]

    # print(*dp, sep='\n')
    # print(digits)
    return (x + 1) - (dp[digits][0] + dp[digits][1])


ans = calc(b) - calc(a - 1)
print(ans)
