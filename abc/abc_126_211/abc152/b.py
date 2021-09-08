a, b = map(int, input().split())
ans = str(a) * b if a < b else str(b) * a
print(ans)
