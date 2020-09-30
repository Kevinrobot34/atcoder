n, x, m = map(int, input().split())

a_l = [x]
a_s = set(a_l)
while True:
    y = (a_l[-1]**2) % m
    if y in a_s:
        break
    a_l.append(y)
    a_s.add(y)

ans = sum(a_l) * (n // len(a_l)) + sum(a_l[:n % len(a_l)])
print(ans)
