from bisect import bisect_left, bisect_right
n = int(input())
xyp = [tuple(map(int, input().split())) for _ in range(n)]
x_list = sorted(list(set(x for x, _, _ in xyp)))
y_list = sorted(list(set(y for _, y, _ in xyp)))
print(x_list)
print(y_list)

nx = len(x_list)
ans = [float('inf')] * (n + 1)
for bit in range(1 << nx):
    cand = [-1] * n
    x_rails = [-float('inf'), 0, float('inf')]
    m = 0
    for i in range(n):
        if (bit >> i) & 1:
            x_rails.append(x_list[i])
            m += 1
    x_rails.sort()
    tmp_si = [0] * n
    for i, (x, y, p) in enumerate(xyp):
        j1 = bisect_left(x_rails, x)
        tmp_si[i] = min(abs(x), abs(y), x_rails[j1] - x, x - x_rails[j1 - 1])
        tmp_si[i] *= p

    print(bin(bit))
    print(tmp_si)

    ans[m] = min(ans[m], sum(tmp_si))
    for bit2 in range(1 << (n - m)):
        y_rails = [-float('inf'), 0, float('inf')]
        for i in range(n - m):
            if (bit >> i) & 1:
                y_rails.append(y_list[i])
