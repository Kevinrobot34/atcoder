import sys
input = sys.stdin.readline

n, m = map(int, input().split())
st = []
imos = [0] * (n + 1)
for _ in range(m):
    s, t = map(int, input().split())
    s -= 1
    st.append((s, t))
    imos[s] += 1
    imos[t] -= 1

a = [0] * n
for i in range(n):
    imos[i + 1] += imos[i]
    if imos[i] > 1:
        a[i] = 1

a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]

ans = []
for i, (s, t) in enumerate(st):
    if a_cs[t] - a_cs[s] == t - s:
        ans.append(i + 1)
print(len(ans))
if len(ans) > 0:
    print(*ans, sep='\n')
