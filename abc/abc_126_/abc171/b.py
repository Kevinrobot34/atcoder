n, k = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

ans = sum(p[:k])

print(ans)
