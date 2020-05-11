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


l1 = []
l2 = []
for i in range(n):
    fi, mi = bracket(s[i])
    if fi >= 0:
        l1.append((fi, mi))
    else:
        l2.append((fi, mi))

l1.sort(key=lambda x: -x[1])
l2.sort(key=lambda x: -(x[0] - x[1]))
l = l1 + l2
v = 0
for fi, mi in l:
    if v + mi >= 0:
        v += fi
    else:
        v = -1
        break

ans = 'Yes' if v == 0 else 'No'
print(ans)
