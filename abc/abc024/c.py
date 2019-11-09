n, d, k = map(int, input().split())
lr_list = [tuple(map(int, input().split())) for _ in range(d)]

ans = []
for _ in range(k):
    s, t = map(int, input().split())

    l0 = r0 = -1
    for i, (l, r) in enumerate(lr_list):
        if l0 == -1:
            if l <= s <= r:
                l0, r0 = l, r
        elif l <= r0 and l0 <= r:
            l0, r0 = min(l0, l), max(r0, r)

        if l0 <= t <= r0:
            ans.append(i + 1)
            break

print(*ans, sep='\n')
