x, y = map(int, input().split())

ans = 0
z = x
while z <= y:
    ans += 1
    z *= 2

print(ans)
