import sys

input = sys.stdin.readline

h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

cs = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h):
    for j in range(w):
        cs[i + 1][j +
                  1] = cs[i][j + 1] + cs[i + 1][j] - cs[i][j] + int(s[i][j])


def f(i1, j1, i2, j2):
    return cs[i1][j1] - cs[i1][j2] - cs[i2][j1] + cs[i2][j2]


ans = h + w
for bit in range(1 << (h - 1)):
    border = [0]
    cand = 0
    for i in range(h):
        if (bit >> i) & 1:
            border.append(i + 1)
            cand += 1
    border.append(h)

    # 貪欲に縦の線に沿って折る
    j0 = 0
    for j in range(w):
        for i in range(len(border) - 1):
            if f(border[i + 1], j + 1, border[i], j0) > k:
                cand += 1
                j0 = j
                break

    # 最後に残ったピースたちがk以下かチェック
    is_possible = True
    for i in range(len(border) - 1):
        if f(border[i + 1], w, border[i], j0) > k:
            is_possible = False
            break

    if is_possible:
        ans = min(ans, cand)
print(ans)
