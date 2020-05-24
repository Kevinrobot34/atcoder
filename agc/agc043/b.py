n = int(input())
a = list(map(int, list(input())))

b = [abs(a[i] - a[i + 1]) for i in range(n - 1)]

if n > 2:
    ans = abs(b[0] - b[-1])
else:
    ans = b[0]
print(ans)


def func(x):
    if len(x) == 1:
        return x[0]
    else:
        return func([abs(x[i] - x[i + 1]) for i in range(len(x) - 1)])


from itertools import product
for p in product(range(1, 4), repeat=6):
    q = [abs(p[i] - p[i + 1]) for i in range(len(p) - 1)]
    z = func(p)

    # print(p, q, z, z == abs(q[0] - q[-1]))
    if z != abs(q[0] - q[-1]):
        print(p, q, set(q), z, z == abs(q[0] - q[-1]))
