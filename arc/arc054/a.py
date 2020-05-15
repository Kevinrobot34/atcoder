l, x, y, s, d = map(int, input().split())
ans1 = (d - s if d >= s else l + d - s) / (x + y)
if x < y:
    ans2 = (s - d if s >= d else l + s - d) / (y - x)
else:
    ans2 = float('inf')
ans = min(ans1, ans2)
print(ans)
