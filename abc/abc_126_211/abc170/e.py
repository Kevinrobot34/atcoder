from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, q = map(int, input().split())


class pseudo_set():
    def __init__(self):
        self.a = []
        self.b = []

    def __len__(self):
        return len(self.a)

    def insert(self, x):
        heappush(self.a, x)

    def erase(self, x):
        heappush(self.b, x)

    def get_min(self):
        while self.b and self.b[0] == self.a[0]:
            _ = heappop(self.a)
            _ = heappop(self.b)
        if len(self.a) > 0:
            return True, self.a[0]
        else:
            return False, None


MAX = 2 * 10**5
kindergartens = [pseudo_set() for _ in range(MAX)]
kids = []
whole = pseudo_set()
for i in range(n):
    rate, k_id = map(int, input().split())
    k_id -= 1
    kids.append((rate, k_id))
    kindergartens[k_id].insert(-rate)

MAX_RATE = 10**10
for i in range(MAX):
    if len(kindergartens[i]) > 0:
        _, tmp_rate = kindergartens[i].get_min()
        tmp_rate *= -1
        whole.insert(tmp_rate)

for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    rate, d_old = kids[c]
    # print(c, d_old, d)

    flag, tmp_rate_old = kindergartens[d_old].get_min()
    if flag:
        tmp_rate_old *= -1
    else:
        tmp_rate_old = -1
    kindergartens[d_old].erase(-rate)
    flag, tmp_rate_new = kindergartens[d_old].get_min()
    if flag:
        tmp_rate_new *= -1
    else:
        tmp_rate_new = -1

    if tmp_rate_old != tmp_rate_new:
        whole.erase(tmp_rate_old)
        if tmp_rate_new != -1:
            whole.insert(tmp_rate_new)

    flag, tmp_rate_old = kindergartens[d].get_min()
    if flag:
        tmp_rate_old *= -1
    else:
        tmp_rate_old = -1
    kindergartens[d].insert(-rate)
    flag, tmp_rate_new = kindergartens[d].get_min()
    if flag:
        tmp_rate_new *= -1
    else:
        tmp_rate_new = -1
    if tmp_rate_old != tmp_rate_new:
        if tmp_rate_old != -1:
            whole.erase(tmp_rate_old)
        whole.insert(tmp_rate_new)

    kids[c] = (rate, d)

    _, tmp_rate = whole.get_min()
    print(tmp_rate)
