n, k = map(int, input().split())

d = set()
ans = n
while n not in d:
    d.add(n)
    if n > k:
        n = n % k
    else:
        n = k - n
    ans = min(ans, n)

print(ans)
