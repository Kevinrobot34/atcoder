s = input()
t = "ATGC"

ans = 0
x = 0
for i in range(len(s)):
    if s[i] in t:
        x += 1
    else:
        x = 0
    ans = max(ans, x)

print(ans)
