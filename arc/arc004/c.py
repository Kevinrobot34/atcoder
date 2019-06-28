x, y = map(int, input().split('/'))

impossible = True

for i in [0, 1]:
    n = int(2 * x / y) + i

    if (n * x) % y == 0:
        m = n*(n+1)//2 - (n*x)//y
        if 1 <= m and m <= n:
            print("{} {}".format(n, m))
            impossible = False

if impossible:
    print("Impossible")
