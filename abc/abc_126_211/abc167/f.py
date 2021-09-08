import sys
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = [input() for _ in range(n)]


def bracket(x):
    # f: final sum of brackets '(':+1, ')': -1
    # m: min value of f
    f = m = 0
    for i in range(len(x)):
        if x[i] == '(':
            f += 1
        else:
            f -= 1
        m = min(m, f)
    # m <= 0
    return f, m


def func(l):
    # l = [(f, m)]
    l.sort(key=lambda x: -x[1])
    v = 0
    for fi, mi in l:
        if v + mi >= 0:
            v += fi
        else:
            return -1
    return v


l1 = []
l2 = []
for i in range(n):
    fi, mi = bracket(s[i])
    if fi >= 0:
        l1.append((fi, mi))
    else:
        l2.append((-fi, mi - fi))

v1 = func(l1)
v2 = func(l2)
if v1 == -1 or v2 == -1:
    ans = 'No'
else:
    ans = 'Yes' if v1 == v2 else 'No'

print(ans)
