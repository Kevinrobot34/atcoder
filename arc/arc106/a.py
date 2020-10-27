n = int(input())

is_possible = False
y = 1
for b in range(1, n):
    y *= 5
    if y >= n:
        break

    a = 0
    x = n - y
    while x % 3 == 0:
        a += 1
        x //= 3

    if x == 1 and a > 0:
        is_possible = True
        break

if is_possible:
    print(a, b)
else:
    print(-1)
