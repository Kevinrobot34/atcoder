MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))

n_bit = max(a).bit_length()
b = [(1 << j) % MOD for j in range(n_bit)]

ans = 0
bit = [0] * n_bit
for i in range(n):
    for j in range(n_bit):
        if (a[i] >> j) & 1:
            ans += b[j] * (i - bit[j])
            bit[j] += 1
        else:
            ans += b[j] * bit[j]
        ans %= MOD

print(ans)
