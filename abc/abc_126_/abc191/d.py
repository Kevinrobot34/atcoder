def main():
    from decimal import Decimal
    import math
    xc, yc, r = map(Decimal, input().split())
    xc, _ = math.modf(xc)
    yc, _ = math.modf(yc)

    ans = 0
    for y in range(math.floor(yc - r) - 2, math.ceil(yc + r) + 2):
        y = Decimal(y)
        if r**2 < (y - yc)**2:
            continue
        d = (r**2 - (y - yc)**2).sqrt()

        xl = math.floor(xc - d - 1)
        while (xl - xc)**2 + (y - yc)**2 > r**2:
            xl += 1

        xr = math.ceil(xc + d + 1)
        while (xr - xc)**2 + (y - yc)**2 > r**2:
            xr -= 1
        xr += 1

        ans += xr - xl

    print(int(ans))


main()
