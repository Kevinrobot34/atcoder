n = int(input())
a = [input() for _ in range(n)]

s = ''
is_possible = True
for i in range(n // 2):
    cand = set(a[n - 1 - i])
    for j in range(n):
        if a[i][j] in cand:
            s += a[i][j]
            break
    if len(s) != i + 1:
        is_possible = False
        break

if is_possible:
    if n % 2 == 0:
        ans = s + s[::-1]
    else:
        ans = s + a[n // 2][0] + s[::-1]
else:
    ans = '-1'

print(ans)
