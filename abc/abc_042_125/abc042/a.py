a, b, c = map(int, input().split())

if a + b + c == 17:
    if (a == 5 and b == 5) or (b == 5 and c == 5) or (c == 5 and a == 5):
        ans = "YES"
    else:
        ans = "NO"
else:
    ans = "NO"

print(ans)
