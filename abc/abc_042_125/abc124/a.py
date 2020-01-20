a, b = map(int, input().split())

if a == b:
  ans = a*2
else:
  ans = max(a, b) * 2 - 1

print(ans)
