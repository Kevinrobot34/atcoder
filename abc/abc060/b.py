a, b, c = map(int, input().split())

if a % b == 0:
    if c == 0:
        ans = "YES"
    else:
        ans = "NO"
else:
    ans = "NO"
    for i in range(1, b+1):
        if (a*i) % b == c:
            ans = "YES"
            break

print(ans)
