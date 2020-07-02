def warshall_floyd(d, n, inf):
    # d        : nxn adjacent matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # if d[i][k] == inf or d[k][j] == inf:
                #     continue
                cand1 = d[i][k] * d[k][j]
                if d[i][j] > cand1:
                    d[i][j] = cand1


n = int(input())
lms = []
units = set()
for _ in range(n):
    l, m, s = input().split()
    m = int(m)
    lms.append((l, m, s))
    units.add(l)
    units.add(s)

units = list(units)
units.sort()
n_units = len(units)
unit_to_i = {u: i for i, u in enumerate(units)}

INF = float('inf')
d = [[INF] * n_units for _ in range(n_units)]
for i in range(n_units):
    d[i][i] = 1

for l, m, s in lms:
    d[unit_to_i[l]][unit_to_i[s]] = m
    d[unit_to_i[s]][unit_to_i[l]] = 1.0 / m

warshall_floyd(d, n_units, INF)
max_m = 0
ans = ''
for i in range(n_units):
    for j in range(n_units):
        if d[i][j] != INF and d[i][j] > max_m:
            max_m = d[i][j]
            ans = f'1{units[i]}={round(d[i][j] + 0.001)}{units[j]}'

# print(units)
# print(*d, sep='\n')
# print(max_m)
print(ans)
