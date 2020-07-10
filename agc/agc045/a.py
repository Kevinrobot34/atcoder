def msb(x):
    cnt = 0
    while x:
        x >>= 1
        cnt += 1
    return cnt


def solve(n, a, s):
    # dp[i] = (i回目時点で最終的に0にできる数の集合)
    dp = [[] for _ in range(n + 1)]
    # dp[n] = [0]
    for i in reversed(range(n)):
        if s[i] == '0':
            x = a[i]
            dp[i] = dp[i + 1].copy()
            dp[i].sort(reverse=True)
            for j in range(len(dp[i])):
                x = min(x, x ^ dp[i][j])
            if x != 0:
                dp[i].append(x)
        else:
            x = a[i]
            dp[i + 1].sort(reverse=True)
            for j in range(len(dp[i + 1])):
                x = min(x, x ^ dp[i + 1][j])
            if x == 0:
                dp[i] = dp[i + 1].copy()
            else:
                return '1'
        # print(i, a[i], s[i], dp[i])
    # print(n, a, s)
    # print(*dp, sep='\n')
    if len(dp[0]) != 0:
        return '0'
    else:
        return '1'


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    ans = solve(n, a, s)
    print(ans)
