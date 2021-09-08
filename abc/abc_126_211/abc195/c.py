n = int(input())
ans = 0
base = 10**3
while base <= n:
    ans += n - base + 1
    base *= 10**3
print(ans)
