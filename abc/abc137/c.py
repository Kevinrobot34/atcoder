n = int(input())
s = [input() for _ in range(n)]

for i in range(n):
    s[i] = [s[i][j] for j in range(len(s[i]))]
    s[i].sort()
    s[i] = ''.join(s[i])

s.sort()
s.append("x")
ans = 0
x = 0
y = "x"
for i in range(len(s)):
    if s[i] == y:
        x += 1
    else:
        ans += x * (x-1) // 2
        y = s[i]
        x = 1

print(ans)
