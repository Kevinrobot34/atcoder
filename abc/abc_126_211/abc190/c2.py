from itertools import product

n, m = map(int, input().split())
ab = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

ans = 0
for p in product(*cd):
    cnt = [0] * n
    for pi in p:
        cnt[pi] += 1
    cand = sum(1 for ai, bi in ab if cnt[ai] > 0 and cnt[bi] > 0)
    ans = max(ans, cand)

print(ans)
