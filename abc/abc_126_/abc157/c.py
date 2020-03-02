n, m = map(int, input().split())
a = [-1] * n

is_possible = True
for i in range(m):
    s, c = map(int, input().split())
    s -= 1
    if a[s] == -1:
        a[s] = c
    elif a[s] != c:
        is_possible = False

if n > 1 and a[0] == 0:
    is_possible = False

if is_possible:
    if a[0] == -1:
        if n > 1:
            a[0] = 1
        else:
            a[0] = 0

    for i in range(1, n):
        if a[i] == -1:
            a[i] = 0
    ans = ''.join([str(ai) for ai in a])
else:
    ans = -1

print(ans)
