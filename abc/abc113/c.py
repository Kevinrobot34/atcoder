n, m = map(int, input().split())

towns = []  # List of (p, y, i)

for i in range(m):
    p, y = map(int, input().split())
    towns.append([p, y, i])

towns = sorted(towns, key=lambda tup: (tup[0], tup[1]))

p_cur = 0
x = 1
for i in range(m):
    if (towns[i][0] == p_cur):
        x += 1
    else:
        x = 1
        p_cur = towns[i][0]

    towns[i][1] = x

towns = sorted(towns, key=lambda tup: tup[2])

for i in range(m):
    print('{:06d}{:06d}'.format(towns[i][0], towns[i][1]))
