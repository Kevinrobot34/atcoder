a, b, c = map(int, input().split())
ans = "bust" if a + b + c >= 22 else "win"
print(ans)
