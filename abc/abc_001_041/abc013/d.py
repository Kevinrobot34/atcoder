n, m, d = map(int, input().split())
a = tuple(map(int, input().split()))
amida = list(range(n))
for ai in a:
    print(amida)
    amida[ai - 1], amida[ai] = amida[ai], amida[ai - 1]

print(amida)
