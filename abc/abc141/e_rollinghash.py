class RollingHash:
    def __init__(self, s: str, base: int=1007, mod: int=10**9+7):
        self.s = s
        self.n = len(s)
        self.base = base
        self.mod = mod

        # preprocess
        self.hash_cum = [0] * (self.n + 1) # hash_cum[i] = (hash of s[:i])
        self.base_pow = [1] * (self.n + 1) # base_pow[i] = base ** i
        for i in range(self.n):
            self.hash_cum[i+1] = (self.hash_cum[i] * base + ord(s[i])) % mod
            self.base_pow[i+1] = (self.base_pow[i] * base) % mod

    def get_hash(self, l: int, r: int) -> int:
        hash_val = self.hash_cum[r] - self.hash_cum[l] * self.base_pow[r-l] % self.mod
        if hash_val < 0:
            hash_val += self.mod
        return hash_val


class RollingHashMulti:
    def __init__(self, s: str, base_list: list=[1007, 2009], mod_list: list=[10**9+7, 10**9+9]):
        self.n = len(base_list)
        self.base_list = base_list
        self.rh_list = [RollingHash(s, base_list[i], mod_list[i]) for i in range(self.n)]

    def get_hash(self, l: int, r: int) -> tuple:
        return tuple( self.rh_list[i].get_hash(l, r) for i in range(self.n) )



n = int(input())
s = input()

rh = RollingHashMulti(s)

def check(x):
    hash_dict = dict()
    for i in range(n-x+1):
        hash_val = rh.get_hash(i, i+x)
        if hash_val in hash_dict:
            if i - hash_dict[hash_val] >= x:
                return True
        else:
            hash_dict[hash_val] = i
    return False


lb = 0
ub = n // 2 + 1
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        lb = mid
    else:
        ub = mid

print(lb)
