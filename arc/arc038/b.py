import sys
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
s = [input() for _ in range(h)]

memo = [[None] * w for _ in range(h)]


def judge(i, j):
    # (i, j)に駒がある状態から開始した時に先手が勝つかどうか
    if i >= h or j >= w or s[i][j] == '#':
        return 'First'
    if memo[i][j]:
        return memo[i][j]

    res = 'Second'
    if judge(i + 1, j) == 'Second':
        res = 'First'
    if judge(i + 1, j + 1) == 'Second':
        res = 'First'
    if judge(i, j + 1) == 'Second':
        res = 'First'
    memo[i][j] = res
    return res


ans = judge(0, 0)
print(ans)
