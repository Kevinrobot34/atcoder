n, k, q = map(int, input().split())
a = list(map(int, input().split()))
a.append(-1)

ans = 10**10
for i in range(n):
    y_cand = []
    c = []
    for j in range(n + 1):
        if a[j] >= a[i]:
            c.append(a[j])
        else:
            c.sort()
            y_cand.extend(c[:max(0, len(c) - k + 1)])
            c = []
    y_cand.sort()
    if len(y_cand) >= q:
        ans = min(ans, y_cand[q - 1] - y_cand[0])

print(ans)
