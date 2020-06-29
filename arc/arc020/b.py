n, cost = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 10**6
for c0 in range(1, 11):
    for c1 in range(1, 11):
        if c0 == c1:
            continue
        cand = 0
        for i in range(n):
            if i % 2 == 0 and a[i] != c0:
                cand += cost
            elif i % 2 == 1 and a[i] != c1:
                cand += cost
        ans = min(ans, cand)

print(ans)
