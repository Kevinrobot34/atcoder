a, b, x = map(int, input().split())

ans = 0
if a * (10**9) + b * 10 <= x:
    ans = 10**9
else:
    for i in range(1, 10):
        if x > b * i:
            cand = (x - b * i) // a
            # print(i, cand)
            if 10**(i - 1) <= cand < 10**i:
                ans = max(ans, cand)
            elif cand >= 10**i:
                ans = max(ans, (10**i) - 1)

print(ans)
