a, b, c = map(int, input().split())

if a + b == c or b + c == a or c + a == b:
    ans = "Yes"
else:
    ans = "No"

print(ans)
