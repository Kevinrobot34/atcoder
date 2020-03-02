def GCD(a: int, b: int) -> int:
    return a if b == 0 else GCD(b, a % b)


def LCM(a: int, b: int) -> int:
    return a * b // GCD(a, b)


MOD = 10**9 + 7
n = int(input())
a = tuple(map(int, input().split()))

MAX_a = max(a)
iinv = [1] * (MAX_a + 1)
for i in range(2, MAX_a + 1):
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD

lcm = 1
for i in range(n):
    lcm = LCM(lcm, a[i])

lcm %= MOD

ans = 0
for i in range(n):
    ans += lcm * iinv[a[i]]
    ans %= MOD

print(ans)
