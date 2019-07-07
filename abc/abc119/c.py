n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

ans = 3000
for bits in range(4**n):
    xa = xb = xc = 0
    tmp_ans = 0
    for i in range(n):
        f = (bits//(4**i)) % 4
        if f == 1:
            if xa != 0:
                tmp_ans += 10
            xa += l[i]
        elif f == 2:
            if xb != 0:
                tmp_ans += 10
            xb += l[i]
        elif f == 3:
            if xc != 0:
                tmp_ans += 10
            xc += l[i]

    if xa == 0 or xb == 0 or xc == 0:
        continue
    
    tmp_ans += abs(a - xa) + abs(b - xb) + abs(c - xc)
    ans = min(ans, tmp_ans)

print(ans)
