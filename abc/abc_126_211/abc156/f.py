import sys
input = sys.stdin.readline

k, q = map(int, input().split())
d = tuple(map(int, input().split()))


def query(n, x, m):
    dd = tuple(di % m for di in d)
    ans = n - 1

    a0 = a1 = x
    for i in range(k):
        a1 += (((n - 1) - (i + 1)) // k + 1) * dd[i]
        if dd[i] == 0:
            ans -= ((n - 1) - (i + 1)) // k + 1

    ans -= (a1 // m) - (a0 // m)

    return ans


for _ in range(q):
    n_i, x_i, m_i = map(int, input().split())
    ans_i = query(n_i, x_i, m_i)
    print(ans_i)
