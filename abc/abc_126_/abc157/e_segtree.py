class SegmentTree1():
    """
    1-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, op_func):
        self.n = 1 << (n_ - 1).bit_length()  # size
        self.data = [ele_id] * (2 * self.n)  # binary tree (1-indexed)
        self.ele_id = ele_id  # identity element
        self.op_func = op_func  # binary operation of monoid

    def __getitem__(self, i):
        return self.data[i + self.n]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n] = data_init[i]  # set data in leaf
        for i in reversed(range(self.n)):
            self.data[i] = self.op_func(self.data[2 * i], self.data[2 * i + 1])

    def update(self, i, x):
        # change i-th element to x (i : 0-indexed)
        i += self.n
        self.data[i] = x
        while i > 1:
            i = i >> 1  # go to parenet-node
            self.data[i] = self.op_func(self.data[2 * i], self.data[2 * i + 1])

    def query(self, l, r):
        # query for interval [l, r) (l, r : 0-indexed)
        l += self.n
        r += self.n
        ret = self.ele_id
        while l < r:
            if l & 1:  # right child
                ret = self.op_func(ret, self.data[l])
                l += 1
            if r & 1:  # right child
                r -= 1
                ret = self.op_func(ret, self.data[r])
            # go to parent-nodes
            l = l >> 1
            r = r >> 1
        return ret


n = int(input())
s = input()

# construct segment tree
ele_id = 0
op_func = lambda a, b: a | b
st_bitset = SegmentTree1(n, ele_id, op_func)
st_bitset.build([1 << (ord(si) - ord('a')) for si in s])

# query
q = int(input())
for _ in range(q):
    k, a, b = input().split()
    k = int(k)
    a = int(a)
    if k == 1:
        b = ord(b) - ord('a')
        a -= 1
        # type1: update
        st_bitset.update(a, 1 << b)
    else:
        # type2: calc
        b = int(b)
        a -= 1
        cnt = bin(st_bitset.query(a, b)).count('1')
        print(cnt)
