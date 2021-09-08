class RollingHash:
    def __init__(self, s: list, base: int = 1007, mod: int = 10**9 + 7):
        self.s = s
        self.n = len(s)
        self.base = base
        self.mod = mod

        # preprocess
        self.h_cum = [0] * (self.n + 1)  # h_cum[i] = (hash of s[:i])
        self.b_pow = [1] * (self.n + 1)  # b_pow[i] = base ** i
        for i in range(self.n):
            self.h_cum[i + 1] = (self.h_cum[i] * base + s[i]) % mod
            self.b_pow[i + 1] = (self.b_pow[i] * base) % mod

    def get_hash(self, l: int, r: int) -> int:
        # get hash value of the substring s[l:r]
        hash_val = self.h_cum[r] - self.h_cum[l] * self.b_pow[r - l] % self.mod
        if hash_val < 0:
            hash_val += self.mod
        return hash_val


n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

a_xor = [a[i % n] ^ a[(i + 1) % n] for i in range(n * 2)]
b_xor = [b[i % n] ^ b[(i + 1) % n] for i in range(n * 2)]

a_xor_rh = RollingHash(a_xor)
b_xor_rh = RollingHash(b_xor)

b_hash = b_xor_rh.get_hash(0, n)
for k in range(n):
    if a_xor_rh.get_hash(k, k + n) == b_hash:
        x = a[k] ^ b[0]
        print(k, x)
