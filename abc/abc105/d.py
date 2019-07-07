from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

a_cs = [0] * (n+1)
for i in range(n):
    a_cs[i+1] = (a_cs[i] + a[i]) % m

d = defaultdict(int)
for i in range(1, n+1):
    d[a_cs[i]] += 1

ans = 0
for k, v in d.items():
    if k == 0:
        ans += v * (v+1) // 2
    else:
        if d[k] > 1:
            ans += (v-1) * v // 2

print(ans)
