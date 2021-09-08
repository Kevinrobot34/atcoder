from heapq import heappush, heappop
from operator import itemgetter
import sys
input = sys.stdin.readline


class PseudoSet():
    def __init__(self):
        self.s = []  # set
        self.e = []  # erase candidate

    def insert(self, x):
        heappush(self.s, x)

    def erase(self, x):
        heappush(self.e, x)

    def get_min(self):
        while self.e and self.e[0] == self.s[0]:
            _ = heappop(self.s)
            _ = heappop(self.e)
        return self.s[0] if len(self.s) > 0 else None


n, q = map(int, input().split())
events = []
for i in range(n):
    s, t, x = map(int, input().split())
    events.append((s - x, +1, x))
    events.append((t - x, -1, x))
for i in range(q):
    d = int(input())
    events.append((d, 2, i))

ans = [-1] * q
events.sort(key=itemgetter(0, 1))
# print(events)
ps = PseudoSet()
for c, t, z in events:
    if t == 1:
        ps.insert(z)
    elif t == -1:
        ps.erase(z)
    else:
        # t == 2
        m = ps.get_min()
        if m is not None:
            ans[z] = m

print(*ans, sep='\n')
