a, k = map(int, input().split())

TARGET = 2 * (10**12)
if k == 0:
    ans = TARGET - a
else:
    ans = 0
    while a < TARGET:
        a += 1 + k * a
        ans += 1

print(ans)
