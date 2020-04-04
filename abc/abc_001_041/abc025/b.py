n, a, b = map(int, input().split())
x = 0
for _ in range(n):
    s, d = input().split()
    d = int(d)

    d = min(max(d, a), b)
    if s == 'East':
        x += d
    else:
        # s == 'West'
        x -= d

if x > 0:
    print('East', x)
elif x == 0:
    print(0)
else:
    # x < 0
    print('West', abs(x))
