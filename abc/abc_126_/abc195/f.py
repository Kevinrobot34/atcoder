a, b = map(int, input().split())
primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71
]
x = [
    sum(1 << i for i, pi in enumerate(primes) if c % pi == 0)
    for c in range(a, b + 1)
]
dp = [0] * (1 << len(primes))
# dp[i] = (含まれている素因数の集合がiであるようなカードの選び方の数)
dp[0] = 1

ans = 0
for c in range(a, b + 1):
    for bit in range(1 << len(primes)):
        if bit & x[c - a] == 0:
            dp[bit | x[c - a]] += dp[bit]

ans = sum(dp)
print(ans)
