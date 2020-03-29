n, m = map(int, input().split())
if n > 12:
    n -= 12
deg_min = m * 6.0
deg_hour = n * 30 + m * 0.5

ans = min(abs(deg_min - deg_hour), 360.0 - abs(deg_min - deg_hour))
print(ans)
