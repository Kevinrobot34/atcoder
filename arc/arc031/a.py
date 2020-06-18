s = input()
n = len(s)

is_kaibun = True
for i in range(n):
    if s[i] != s[n - 1 - i]:
        is_kaibun = False
        break

ans = 'YES' if is_kaibun else 'NO'
print(ans)
