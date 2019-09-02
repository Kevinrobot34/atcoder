a, b, c = map(int, input().split())

ans = max(10*a+b+c, a+10*b+c, a+b+10*c)
print(ans)
