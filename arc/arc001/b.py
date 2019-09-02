a, b = map(int, input().split())
c = abs(a - b)

ans = 0
ans += c // 10
c =  c % 10

if c <= 3:
    ans += c
elif c <= 7:
    ans += 1 + abs(c - 5)
else:
    ans += 1 + abs(c - 10)

print(ans)
