a, b, c = map(int, input().split())

ans = 0
ans += min(c, a+b+1)
ans += b

print(ans)
