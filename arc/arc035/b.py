from collections import Counter
MOD = 10**9 + 7
n = int(input())
t = [int(input()) for _ in range(n)]
t.sort()

ans1 = 0
for i in range(n):
    ans1 += t[i] * (n - i)

fact = [1] * (n + 1)
for i in range(2, n + 1):
    fact[i] = (fact[i - 1] * i) % MOD

ans2 = 1
t_count = Counter(t)
for v in t_count.values():
    ans2 *= fact[v]
    ans2 %= MOD

print(ans1)
print(ans2)
