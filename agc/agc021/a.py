n = input()

ans = 0
s = 0
for i in range(len(n)):
    ans = max(ans, s + int(n[i]) - 1 + 9 * (len(n) - i - 1))
    s += int(n[i])
ans = max(ans, s)

print(ans)
