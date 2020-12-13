n, k, m, r = map(int, input().split())
scores = [int(input()) for _ in range(n - 1)]
scores.sort(reverse=True)

if sum(scores[:k]) >= k * r:
    ans = 0
else:
    ans = k * r - sum(scores[:k - 1])
    if ans > m:
        ans = -1

print(ans)
