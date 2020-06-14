class RollingHash2D:
    def __init__(self, s, n, m, b=1007, c=2009, mod=10**9 + 7):
        self.s = s
        self.n = n
        self.m = m
        self.b = b
        self.c = c
        self.mod = mod

        # preprocess
        self.hash_cs = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        self.b_pow = [1] * (self.n + 1)  # base_pow[i] = base ** i
        self.c_pow = [1] * (self.m + 1)  # base_pow[i] = base ** i
        for i in range(self.n):
            self.b_pow[i + 1] = (self.b_pow[i] * self.b) % mod
        for i in range(self.m):
            self.c_pow[i + 1] = (self.c_pow[i] * self.c) % mod

        for i in range(self.n):
            for j in range(self.m):
                self.hash_cs[i + 1][j + 1] = \
                    self.hash_cs[i + 1][j] * self.c \
                    + self.hash_cs[i][j + 1] * self.b \
                    - self.hash_cs[i][j] * self.b * self.c \
                    + self.s[i][j]
                self.hash_cs[i + 1][j + 1] %= self.mod

    def calc_rolling_hash(self, il: int, ir: int, jl: int, jr: int) -> int:
        hash_val = \
            self.hash_cs[ir][jr] \
             - self.hash_cs[ir][jl] * self.c_pow[jr-jl] \
             - self.hash_cs[il][jr] * self.b_pow[ir-il] \
             + self.hash_cs[il][jl] * self.b_pow[ir-il] * self.c_pow[jr-jl]
        hash_val %= self.mod
        return hash_val

    def calc_hash(self, t, nt, mt):
        h = 0
        for i in range(nt):
            for j in range(mt):
                h += t[i][j] * self.b_pow[nt - i - 1] * self.c_pow[mt - j - 1]
                h %= self.mod
        return h


n, m = map(int, input().split())
a = [list(map(ord, list(input()))) for _ in range(n)]
b = [list(map(ord, list(input()))) for _ in range(m)]

rh = RollingHash2D(a, n, n)
b_hash = rh.calc_hash(b, m, m)
flag = False
for i in range(n - m + 1):
    for j in range(n - m + 1):
        if rh.calc_rolling_hash(i, i + m, j, j + m) == b_hash:
            flag = True
            break
    if flag:
        break

ans = 'Yes' if flag else 'No'
print(ans)
