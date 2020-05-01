from collections import defaultdict
n, x = map(int, input().split())
w = tuple(int(input()) for _ in range(n))
m = n // 2
ans = 0

cand = defaultdict(int)
for bit in range(1 << m):
    s = sum(w[i] for i in range(m) if (bit >> i) & 1)
    cand[s] += 1

for bit in range(1 << (n - m)):
    s = sum(w[m + i] for i in range(n - m) if (bit >> i) & 1)
    ans += cand[x - s]

print(ans)
