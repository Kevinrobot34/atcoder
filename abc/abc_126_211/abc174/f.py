from operator import itemgetter
import sys
input = sys.stdin.readline


class BIT1():
    """
    Binary Indexed Tree (1-indexed)
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (self.n + 1)
        self.data = [0] * (self.n + 1)

    def add(self, idx, x):
        # add x to idx-th element
        # idx: 1-indexed
        self.data[idx] += x
        while idx <= self.n:
            self.bit[idx] += x
            idx += idx & (-idx)

    def sum(self, idx):
        # get sum of [1, idx]
        # idx: 1-indexed
        s = 0
        while idx:
            s += self.bit[idx]
            idx -= idx & (-idx)
        return s


def main():
    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    queries = []
    for i in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        queries.append((i, l, r))
    queries.sort(key=itemgetter(2))

    query_counter = 0
    ans = [0] * q
    # last_visit[i] = 色iの良い玉のindex
    last_visit = [-1] * (n + 1)
    # bit[i] = iの位置に何個の良い玉があるか
    bit = BIT1(n)
    for i, ci in enumerate(c):
        if last_visit[ci] != -1:
            bit.add(last_visit[ci] + 1, -1)

        last_visit[ci] = i
        bit.add(i + 1, +1)

        while query_counter < q and queries[query_counter][2] == i:
            idx, l, r = queries[query_counter]
            ans[idx] = bit.sum(r + 1) - bit.sum(l)
            query_counter += 1

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
