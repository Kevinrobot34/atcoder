n = int(input())
a = list(map(int, input().split()))

MOD = 10**9 + 7
a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]
    a_cs[i + 1] %= MOD

ans = sum(a_cs[i] * a[i] % MOD for i in range(n))
ans %= MOD
print(ans)
