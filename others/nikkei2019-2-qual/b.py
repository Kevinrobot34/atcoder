from collections import defaultdict
MOD = 998244353

n = int(input())
d = list(map(int, input().split()))

cnt = defaultdict(int)
m = 0
for i in range(n):
    cnt[d[i]] += 1
    m = max(d[i], m)

if d[0] != 0 or cnt[0] != 1:
    ans = 0
else:
    ans = 1
    for i in range(1, m + 1):
        ans *= cnt[i - 1]**cnt[i]
        ans %= MOD

print(ans)
