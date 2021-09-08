n, m, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ab.append([t, t])

is_possible = True
b_prev = 0
c = n
for a, b in ab:
    c -= a - b_prev
    if c <= 0:
        is_possible = False

    c = min(n, c + b - a)
    b_prev = b

ans = 'Yes' if is_possible else 'No'
print(ans)
