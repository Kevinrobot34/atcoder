n, k = map(int, input().split())
p = list(map(int, input().split()))

p_sum = 0
ans = 0
for i in range(n):
    p_sum += p[i]
    if i >= k:
        p_sum -= p[i - k]

    ans = max(p_sum, ans)

ans = (ans + k) / 2

print(ans)
