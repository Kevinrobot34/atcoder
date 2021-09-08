a, b = map(int, input().split())
c, d = map(int, input().split())

x = c - a
y = d - b

if x == y == 0:
    ans = 0
elif x - y == 0 or x + y == 0:
    ans = 1
elif abs(x) + abs(y) <= 3:
    ans = 1
elif abs(x) + abs(y) <= 6:
    ans = 2
elif abs(x - y) <= 3:
    ans = 2
elif abs(x + y) <= 3:
    ans = 2
elif (x + y) % 2 == 0:
    ans = 2
else:
    ans = 3

print(ans)
