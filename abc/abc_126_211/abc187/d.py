n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]
cnt = sum(-ai for ai, bi in ab)

ab.sort(key=lambda x: 2 * x[0] + x[1], reverse=True)
ans = 0
for ai, bi in ab:
    cnt += 2 * ai + bi
    ans += 1
    if cnt > 0:
        break

print(ans)
