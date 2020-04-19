s = input()

n = len(s)
ans = n
for i in range(1, n):
    if s[i - 1] != s[i]:
        # left:  [0, i) -> length = i
        # right: [i, n) -> length = n - i
        ans = min(ans, max(i, n - i))

print(ans)
