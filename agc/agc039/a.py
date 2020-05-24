s = input()
k = int(input())

c = s[0]
l = 1
a = []
for i in range(1, len(s)):
    if s[i] == c:
        l += 1
    else:
        a.append(l)
        c = s[i]
        l = 1
a.append(l)

ans = 0
if len(a) == 1:
    # s consists of one character
    ans += (a[0] * k) // 2
elif s[0] == s[-1]:
    ans += a[0] // 2
    ans += ((a[0] + a[-1]) // 2) * (k - 1)
    for i in range(1, len(a) - 1):
        ans += (a[i] // 2) * k
    ans += a[-1] // 2
else:
    for i in range(len(a)):
        ans += (a[i] // 2) * k

print(ans)
