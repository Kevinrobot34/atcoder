a, b, c = map(int, input().split())

if c - b == b - a:
    ans = "YES"
else:
    ans = "NO"

print(ans)
