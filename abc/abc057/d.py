n, a, b = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
print(n, a, b, v)

ans = 0
pattern = 1
selected = {}
m = 0
s = 0
for i in range(n):
    print(i, v[i])

    if v[i] in selected:
        selected[v[i]] += 1
    else:
        selected[v[i]] = 1
        m += 1
        s += v[i]


    if a <= m <= b and ans <= s / m:
        ans = s / m
        pattern = 1
        for key, val in selected.items():
            pattern *= val

print(ans)
print(pattern)
