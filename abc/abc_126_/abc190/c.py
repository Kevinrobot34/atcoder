n, m = map(int, input().split())
ab = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

ans = 0
for bit in range(1 << k):
    cnt = [0] * n
    for i, (ci, di) in enumerate(cd):
        cnt[ci if (bit >> i) & 1 else di] += 1
    cand = sum(1 for ai, bi in ab if cnt[ai] > 0 and cnt[bi] > 0)
    ans = max(ans, cand)

print(ans)
