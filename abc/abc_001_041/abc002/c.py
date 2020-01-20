xa, ya, xb, yb, xc, yc = map(int, input().split())

dx1 = xb - xa
dy1 = yb - ya

dx2 = xc - xa
dy2 = yc - ya

ans = abs(dx1 * dy2 - dx2 * dy1) / 2.0
print(ans)
