x, k, d = map(int, input().split())

if abs(x) >= k * d:
    ans = abs(x) - k * d
else:
    k -= abs(x) // d
    if k % 2 == 0:
        ans = abs(x) % d
    else:
        ans = d - abs(x) % d

print(ans)
