n = int(input())
a = list(map(int, input().split()))

x = 0
for ai in a:
    if ai == x + 1:
        x += 1

ans = -1 if x == 0 else n - x
print(ans)
