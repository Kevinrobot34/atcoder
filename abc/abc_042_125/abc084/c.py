n = int(input())
c = []
s = []
f = []
for i in range(n-1):
    ci, si, fi = map(int, input().split())
    c.append(ci)
    s.append(si)
    f.append(fi)


for i in range(n-1):
    ans = s[i]
    for j in range(i, n-1):
        if ans < s[j]:
            ans = s[j] + c[j]
        elif ans % f[j] == 0:
            ans += c[j]
        else:
            ans += f[j] - ans % f[j] + c[j]
    print(ans)
print(0)
