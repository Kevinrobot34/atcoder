h, w = map(int, input().split())
a = [input() for _ in range(h)]

a = [ai for ai in a if set(ai) != {'.'}]
a = ["".join([a[i][j] for i in range(len(a))]) for j in range(len(a[0]))]
a = [ai for ai in a if set(ai) != {'.'}]
a = ["".join([a[i][j] for i in range(len(a))]) for j in range(len(a[0]))]

for ai in a:
    print(ai)
