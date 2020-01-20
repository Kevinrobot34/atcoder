MOD = 10**9 + 7

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

w = 0
for i in range(n):
    if (n-1-i) - i <= 0:
        break
    w += (x[n-1-i] - x[i]) * ((n-1-i) - i)
    w %= MOD

h = 0
for i in range(m):
    if (m-1-i) - i <= 0:
        break
    h += (y[m-1-i] - y[i]) * ((m-1-i) - i)
    h %= MOD


ans = (w * h) % MOD

print(ans)
