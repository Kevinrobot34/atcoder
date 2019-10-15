a, b = map(int, input().split())

if a == b:
    ans = "Draw"
elif a == 1:
    ans = "Alice"
elif b == 1:
    ans = "Bob"
elif a > b:
    ans = "Alice"
else:
    ans = "Bob"

print(ans)
