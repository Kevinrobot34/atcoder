n, m, p, q, r = map(int, input().split())

chocolate = [[0] * m for _ in range(n)]
for _ in range(r):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    chocolate[x][y] = z

ans = 0
for bit in range(1 << n):
    bit_list = [(bit >> i) & 1 for i in range(n)]
    if sum(bit_list) != p:
        continue
    cand = [
        sum(chocolate[i][j] * bit_list[i] for i in range(n)) for j in range(m)
    ]
    cand.sort(reverse=True)
    ans = max(ans, sum(cand[:q]))
print(ans)
