from collections import defaultdict
MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))

cnt = defaultdict(int)
cnt[-1] = 3
ans = 1
for i in range(n):
    ans *= max(cnt[a[i] - 1] - cnt[a[i]], 0)
    ans %= MOD

    cnt[a[i]] += 1

print(ans)
