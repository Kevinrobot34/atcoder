n, x, y = map(int, input().split())
x -= 1
y -= 1

ans = [0] * n
for i in range(n):
    for j in range(i + 1, n):
        d = min(abs(i - j),
                abs(i - x) + 1 + abs(y - j),
                abs(i - y) + 1 + abs(x - j))
        ans[d] += 1

for k in range(1, n):
    print(ans[k])
