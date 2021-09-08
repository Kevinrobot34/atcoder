v, t, s, d = map(int, input().split())
ans = 'No' if v * t <= d <= v * s else 'Yes'
print(ans)
