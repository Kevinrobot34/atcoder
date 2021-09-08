n, x, m = map(int, input().split())

a_idx = [-1] * m
a_idx[x] = 0
a = [x]
idx = 1
while True:
    y = (a[-1]**2) % m
    if a_idx[y] != -1:
        i = a_idx[y]
        j = len(a) - i
        break
    else:
        a_idx[y] = idx
        idx += 1
        a.append(y)

ans = sum(a) * (n)
ans = sum(a[:i]) + sum(a[i:]) * ((n - i) // j) + sum(a[i:i + (n - i) % j])
print(ans)
