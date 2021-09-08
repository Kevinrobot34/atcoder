x = int(input())

ans = 0
while x >= 500:
    ans += 1000
    x -= 500
while x >= 5:
    ans += 5
    x -= 5
print(ans)
