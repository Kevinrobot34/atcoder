class BIT1():
    """
    Binary Indexed Tree (1-indexed)
    """
    def __init__(self, n):
        self.n = n  # size
        self.bit = [0] * (self.n + 1)  # bit (1-indexed)
        self.data = [0] * (self.n + 1)  # data (1-indexed)

    def add(self, idx, x):
        # add x to idx-th element  (idx: 1-indexed)
        self.data[idx] += x
        while idx <= self.n:
            self.bit[idx] += x
            idx += (idx & (-idx))

    def sum(self, idx):
        # get sum of [1, idx]  (idx: 1-indexed)
        s = 0
        while idx:
            s += self.bit[idx]
            idx -= (idx & (-idx))
        return s


n = int(input())
s = [ord(si) - ord('a') for si in list(input())]
bit_list = [BIT1(n + 1) for _ in range(26)]
for i in range(n):
    bit_list[s[i]].add(i + 1, +1)

q = int(input())
for _ in range(q):
    k, a, b = input().split()
    k = int(k)
    a = int(a)
    if k == 1:
        b = ord(b) - ord('a')
        # type1: update
        bit_list[s[a - 1]].add(a, -1)
        bit_list[b].add(a, +1)
        s[a - 1] = b
    else:
        # type2: calc
        b = int(b)
        a -= 1
        cnt = 0
        for bit_i in bit_list:
            if bit_i.sum(b) - bit_i.sum(a) > 0:
                cnt += 1
        print(cnt)
