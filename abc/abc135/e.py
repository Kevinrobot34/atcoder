k = int(input())
gx, gy = map(int, input().split())
bx, by = 0, 0

def dist_man(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

if k % 2 == 0 and (gx + gy) % 2 == 1:
    print(-1)
else:
    ans = []
    while dist_man(bx, by, gx, gy) > 2*k:
        if bx + k <= gx:
            bx += k
        elif gx <= bx - k:
            bx -= k
        elif by + k <= gy:
            by += k
        elif gy <= by - k:
            by -= k
        else:
           break
        ans.append((bx, by))
        print((bx, by), dist_man(bx, by, gx, gy))

    if dist_man(bx, by, gx, gy) == k:
        ans.append((gx, gy))
    else:
        if (bx+by)%2 != (gx+gy)%2:
            for i in range(k):


    print(len(ans))
    for x, y in ans:
        print(x, y)
