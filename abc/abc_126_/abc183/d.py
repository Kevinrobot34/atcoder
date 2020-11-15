from operator import itemgetter

n, w = map(int, input().split())
MAX = 2 * (10**5) + 2
imos = [0] * MAX

for _ in range(n):
    s, t, p = map(int, input().split())
    imos[s] += p
    imos[t] -= p

for i in range(MAX - 1):
    imos[i + 1] += imos[i]

ans = 'Yes'
for i in range(MAX - 1):
    if imos[i] > w:
        ans = 'No'
        break

print(ans)
