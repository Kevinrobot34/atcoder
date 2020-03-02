n = int(input())
p = list(map(int, input().split()))

ans = 0
tmp_min = n + 1
for i in range(n):
    if p[i] < tmp_min:
        ans += 1
    tmp_min = min(tmp_min, p[i])

print(ans)
