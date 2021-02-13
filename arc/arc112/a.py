t = int(input())


def func(l, r):
    if 2 * l <= r:
        return (r - 2 * l + 1) * (r - 2 * l + 2) // 2
    else:
        return 0


for _ in range(t):
    l, r = map(int, input().split())
    print(func(l, r))
