n = int(input())
a = list(map(int, input().split()))

two_pow = [1 << i for i in range(n + 1)]
is_possible = True
for i in range(n):
    if a[i] > two_pow[i] - 1:
        is_possible = False
        break
if a[n] > two_pow[n]:
    is_possible = False

s = 0
for i in range(n + 1):
    s += a[i] * two_pow[n - i]
if s > two_pow[n]:
    is_possible = False

b = [0] * (n + 1)
for i in range(n):
    b[i + 1] = (a[i] + b[i]) * 2

c = [0] * (n + 1)
c[n] = a[n]
ans = a[n]
for i in reversed(range(n)):
    if (c[i + 1] + 1) // 2 + a[i] + b[i] > two_pow[i]:
        is_possible = False
        break
    c[i] = min(c[i + 1], two_pow[i] - a[i] - b[i]) + a[i]
    ans += c[i]

# print(a)
# print(b)
# print(c)

if is_possible:
    print(ans)
else:
    print(-1)
