r, b = map(int, input().split())
x, y = map(int, input().split())

# m = (x * b - r) / (x * y - 1)
# n = (y * r - b) / (x * y - 1)

if x * b - r <= 0:
    ans = b
elif y * r - b <= 0:
    ans = r
else:
    # ans = math.floor(m+n)
    m = (x * b - r) // (x * y - 1)
    n = (y * r - b) // (x * y - 1)

    if n * x + (m + 1) <= r and n + (m + 1) * y <= b:
        ans = n + m + 1
    elif (n + 1) * x + m <= r and (n + 1) + m * y <= b:
        ans = n + m + 1
    else:
        ans = n + m

print(ans)
