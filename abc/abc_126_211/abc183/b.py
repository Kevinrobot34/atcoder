sx, sy, gx, gy = map(int, input().split())

a = (gy + sy) / (gx - sx)

ans = sx + sy / a
print(ans)
