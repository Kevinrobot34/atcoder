n, m = map(int, input().split())
cakes = [list(map(int, input().split())) for i in range(n)]

ans = 0
for bit in range(1<<3):
    flip = [(-1)**((bit>>i)&1) for i in range(3)]
    cakes.sort(key=lambda x: sum([x[i] * flip[i] for i in range(3)]), reverse=True)
    v = [sum([cakes[i][j] for i in range(m)]) for j in range(3)]
    ans = max(ans, sum(map(abs, v)))

print(ans)
