MOD = 10**9 + 7
n = int(input())
s = input()

t = []
for i in range(2*n):
    if i % 2 == 0:
        t.append(0 if s[i] == 'B' else 1)
    else:
        t.append(0 if s[i] == 'W' else 1)

# print(t)
ans = 1
l = r = 0
for i in range(2*n):
    if t[i] == 1:
        ans *= max(l - r, 0)
        ans %= MOD

    if t[i] == 0:
        l += 1
    else:
        r += 1

if l == n:
    for i in range(1, n+1):
        ans *= i
        ans %= MOD
else:
    ans = 0

print(ans)
