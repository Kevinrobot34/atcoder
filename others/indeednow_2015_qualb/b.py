s = input()
t = input()
n, m = len(s), len(t)

if n == m:
    ans = -1
    for i in range(n):
        if t == s[n - i:] + s[:n - i]:
            ans = i
            break
else:
    ans = -1

print(ans)
