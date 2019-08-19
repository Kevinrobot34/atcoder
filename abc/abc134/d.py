n = int(input())
a = list(map(int, input().split()))

b = [0] * (n+1)
for i in reversed(range(1, n+1)):
    bi = 0
    for j in range(2, n//i + 1):
        bi += b[i*j]
    bi %= 2

    if bi != a[i-1]:
        b[i] = 1
    else:
        b[i] = 0

b_idx = [str(i) for i in range(1, n+1) if b[i] == 1]
m = len(b_idx)
print(m)
if m > 0:
    print(' '.join(b_idx))
