n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_cs = [0] * (n + 1)
b_cs = [0] * (m + 1)

for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]
for i in range(m):
    b_cs[i + 1] = b_cs[i] + b[i]

ans = 0
j = m
for i in range(n + 1):
    while j > 0 and a_cs[i] + b_cs[j] > k:
        j -= 1

    if a_cs[i] + b_cs[j] <= k:
        ans = max(ans, i + j)

print(ans)
