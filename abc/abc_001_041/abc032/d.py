import sys
input = sys.stdin.readline
n, w = map(int, input().split())
baggage = [list(map(int, input().split())) for _ in range(n)]

v_max = max(baggage[i][0] for i in range(n))
w_max = max(baggage[i][1] for i in range(n))

if n <= 30:
    # 半分全列挙
    from collections import defaultdict
    from bisect import bisect_left, bisect_right

    d = defaultdict(int)
    d[0] = 0
    m = n // 2
    for bit in range(1 << m):
        w_sum = v_sum = 0
        for i in range(m):
            if (bit >> i) & 1:
                v_sum += baggage[i][0]
                w_sum += baggage[i][1]
        d[w_sum] = max(v_sum, d[w_sum])
    w_list = sorted(list(d.keys()))
    v_list = [d[w_list[i]] for i in range(len(w_list))]
    for i in range(1, len(v_list)):
        v_list[i] = max(v_list[i], v_list[i - 1])
    ans = 0
    for bit in range(1 << (n - m)):
        w_sum = v_sum = 0
        for i in range(n - m):
            if (bit >> i) & 1:
                v_sum += baggage[i + m][0]
                w_sum += baggage[i + m][1]
        idx = bisect_right(w_list, w - w_sum)
        if idx > 0:
            ans = max(ans, v_sum + v_list[idx - 1])
elif w_max <= 1000:
    # dp[i+1][w] = (i番目の荷物まで見て、重さがwの時の価値の最大値)
    j_max = w_max * n
    dp = [[0] * (j_max + 1) for _ in range(n + 1)]

    for i, (vi, wi) in enumerate(baggage):
        for j in range(j_max + 1):
            if j + wi <= j_max:
                dp[i + 1][j + wi] = max(dp[i + 1][j + wi], dp[i][j] + vi)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

    ans = max(dp[n][:min(j_max + 1, w + 1)])
else:
    # v_max <=1000
    # dp[i+1][v] = (i番目の荷物まで見て、価値がvの時の最小の重さ)
    j_max = sum(baggage[i][0] for i in range(n))
    dp = [[w + 1] * (j_max + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i, (vi, wi) in enumerate(baggage):
        for j in range(j_max + 1):
            if j + vi <= j_max:
                dp[i + 1][j + vi] = min(dp[i + 1][j + vi], dp[i][j] + wi)
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

    ans = max(j for j in range(j_max) if dp[n][j] <= w)

print(ans)
