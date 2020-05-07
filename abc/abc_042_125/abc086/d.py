import gc
n, k = map(int, input().split())
k2 = k * 2
b = [[0] * (k * 3) for _ in range(k * 3)]
for i in range(n):
    x, y, c = input().split()
    x = int(x) % k2
    y = int(y) % k2
    if c == 'W':
        x = (x + k) % k2

    b[x][y] += 1
    if x < k:
        b[x + k2][y] += 1
    if y < k:
        b[x][y + k2] += 1
    if x < k and y < k:
        b[x + k2][y + k2] += 1

b_cs = [[0] * (k * 3 + 1) for _ in range(k * 3 + 1)]
for i in range(k * 3):
    for j in range(k * 3):
        b_cs[i + 1][j +
                    1] = b_cs[i + 1][j] + b_cs[i][j + 1] - b_cs[i][j] + b[i][j]


def func_b(x, y):
    return b_cs[x + k][y + k] - b_cs[x + k][y] - b_cs[x][y + k] + b_cs[x][y]


# print('black')
# print(*b, sep='\n')
# print(*b_cs, sep='\n')

ans = 0
for i in range(k):
    for j in range(k):
        cand = 0
        cand += func_b(i, j)
        cand += func_b(i + k, j + k)
        # print(i, j, cand)
        ans = max(ans, cand)

        cand = 0
        cand += func_b(i + k, j)
        cand += func_b(i, j + k)
        # print(i, j, cand)
        ans = max(ans, cand)

print(ans)
