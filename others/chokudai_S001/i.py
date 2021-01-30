from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]
ans = 0
for i in range(n):
    idx = bisect_left(a_cs, a_cs[i] + n)
    if idx <= n and a_cs[idx] == a_cs[i] + n:
        ans += 1
print(ans)
