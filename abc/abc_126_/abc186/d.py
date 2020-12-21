n = int(input())
a = list(map(int, input().split()))
a.sort()

a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]

ans = 0
for i in range(n):
    ans += (a_cs[n] - a_cs[i + 1]) - (n - i - 1) * a[i]

print(ans)
