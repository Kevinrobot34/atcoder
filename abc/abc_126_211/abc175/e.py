import sys


def main():
    input = sys.stdin.readline

    r, c, k = map(int, input().split())

    items = [[0] * (c + 1) for _ in range(r + 1)]
    for _ in range(k):
        i, j, v = map(int, input().split())
        items[i][j] = v

    # dp[m][i][j] = (i行j列時点で、i行でm個のitemを取得している時の価値の最大値)
    dp = [[[0] * (c + 1) for _ in range(r + 1)] for _ in range(4)]

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            for m in range(4):
                dp[m][i][j] = max(dp[3][i - 1][j], dp[m][i][j - 1])
            if items[i][j] > 0:
                for m in [2, 1, 0]:
                    dp[m + 1][i][j] = max(dp[m + 1][i][j],
                                          dp[m][i][j] + items[i][j])

    print(dp[3][r][c])


if __name__ == '__main__':
    main()
