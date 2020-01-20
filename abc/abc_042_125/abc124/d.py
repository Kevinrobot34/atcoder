n, k = map(int, input().split())
s = input()

a = [s[0]]
b = [1]
for i in range(1, n):
    if a[-1] != s[i]:
        a.append(s[i])
        b.append(1)
    else:
        b[-1] += 1
if a[0] == '0':
    a = ['1'] + a
    b = [0] + b
if a[-1] == '0':
    a = a + ['1']
    b = b + [0]


ans = cand = 0
for i in range(len(a)):
    cand += b[i]

    if i > 2 * k and i % 2 == 0:
        cand -= b[i-2*k-1] + b[i-2*k-2]

    if i % 2 == 0:
        ans = max(ans, cand)

print(ans)
