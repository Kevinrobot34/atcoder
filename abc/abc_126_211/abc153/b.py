h, n = map(int, input().split())
a = list(map(int, input().split()))

ans = "Yes" if sum(a) >= h else "No"
print(ans)
