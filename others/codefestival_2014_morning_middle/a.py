p, n = input().split()
p = float(p)
n = int(n)

if p == 1.0:
    ans = (1 - pow(-1, n)) / 2
else:
    ans = (1 - pow(1 - 2 * p, n)) / 2
print(ans)
