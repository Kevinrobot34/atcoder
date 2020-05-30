MOD = 10**9 + 7
n = int(input())
a = tuple(map(int, input().split()))

cnt = [0] * n
for i in range(n):
    cnt[a[i]] += 1

if a[0] == 0 and cnt[0] == 1:
    ans = 1
    m = min(n, max(a) + 1)
    for i in range(1, m):
        ans *= pow(pow(2, cnt[i - 1], MOD) - 1, cnt[i], MOD)
        ans %= MOD
        ans *= pow(2, cnt[i] * (cnt[i] - 1) // 2, MOD)
        ans %= MOD
else:
    ans = 0
print(ans)
