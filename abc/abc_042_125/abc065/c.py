n, m = map(int, input().split())

MOD = 10**9 + 7
def fact(x):
    res = 1
    for i in range(2, x+1):
        res *= i
        res %= MOD
    return res

if abs(n - m) > 1:
    ans = 0
elif abs(n - m) == 1:
    ans = (fact(n) * fact(m)) % MOD
else:
    # n == m
    ans = (fact(n) * fact(m) * 2) % MOD

print(ans)
