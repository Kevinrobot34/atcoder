MOD = 10**9 + 7


def modinv(x, mod=MOD):
    return pow(x, mod - 2, mod)


x = int(input())
y = int(input())
z = int(input())

p = z * (x - y)
r = -p / (p + y * x)
q = y * (x - z)
c = -q / (q + z * x)
#
# print(r, c)

r2 = (MOD - p) * modinv((p + y * x) % MOD) % MOD
c2 = (MOD - q) * modinv((q + z * x) % MOD) % MOD
print(r2, c2)
