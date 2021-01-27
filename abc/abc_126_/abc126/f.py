m, k = map(int, input().split())

if k >= (1 << m):
    print(-1)
else:
    if m == 0:
        print(0, 0)
    elif m == 1:
        if k == 0:
            print(0, 0, 1, 1)
        else:
            print(-1)
    else:
        b = [i for i in range(1 << m) if i != k]
        c = b[::-1]
        ans = b + [k] + c + [k]
        print(*ans)
