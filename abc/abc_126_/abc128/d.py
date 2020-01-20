n, k = map(int, input().split())
v = list(map(int, input().split()))


ans = 0
for k1 in range(k+1):
    for k2 in range(k+1):
        if k1 + k2 > k or k1 + k2 > n or k1 > n or k2 > n:
            continue

        w = v[:k1] + v[n-k2:]
        w.sort()
        ans = max(ans, sum(w))
        # print(k1, k2, max(0, k-k1-k2), len(w), w)
        for k3 in range(1, max(0, k-k1-k2)+1):
            ans = max(ans, sum(w[k3:]))

print(ans)
