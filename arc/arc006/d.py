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

    def get_hash(self, il: int, ir: int, jl: int, jr: int) -> int:
        hash_val = \
            self.hash_cs[ir][jr] \
             - self.hash_cs[ir][jl] * self.c_pow[jr-jl] \
             - self.hash_cs[il][jr] * self.b_pow[ir-il] \
             + self.hash_cs[il][jl] * self.b_pow[ir-il] * self.c_pow[jr-jl]
        hash_val %= self.mod
        return hash_val


h, w = map(int, input().split())
c = [list(map(lambda x: ord(x), list(input()))) for _ in range(h)]
s_dict = {}
s_dict['a'] = '''
.......
...o...
..o.o..
.o...o.
.ooooo.
.o...o.
.......
'''
s_dict['b'] = '''
.......
.oooo..
.o...o.
.oooo..
.o...o.
.oooo..
.......
'''
s_dict['c'] = '''
.......
..ooo..
.o...o.
.o.....
.o...o.
..ooo..
.......
'''

for k in s_dict:
    pass
