n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
ans = float('inf')
for i, (ai, bi) in enumerate(ab):
    ans = min(ans, ai + bi)
    for j, (aj, bj) in enumerate(ab):
        if i == j:
            continue
        ans = min(ans, max(ai, bj), max(aj, bi))

print(ans)
