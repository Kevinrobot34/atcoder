from itertools import product

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

is_found = False
for p in product(range(k), repeat=n):
    x = 0
    for i, pi in enumerate(p):
        x = x ^ t[i][pi]

    if x == 0:
        is_found = True
        break

ans = "Found" if is_found else "Nothing"
print(ans)
