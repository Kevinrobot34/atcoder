n = int(input())
x = input()

x_cnt = x.count('1')
yp = 0
ym = 0
for i in range(n):
    yp *= 2
    yp += int(x[i])
    yp %= x_cnt + 1

    if x_cnt != 1:
        ym *= 2
        ym += int(x[i])
        ym %= x_cnt - 1


def count(z):
    cnt = 0
    while z:
        z = z % bin(z).count('1')
        cnt += 1
    return cnt


# print(x, x_cnt, yp, ym)

ans = [0] * n
bp = bm = 1
for i in reversed(range(n)):
    if x[i] == '0':
        z = (yp + bp) % (x_cnt + 1)
        ans[i] = 1 + count(z)
    else:
        if x_cnt == 1:
            ans[i] = 0
        else:
            z = (ym - bm + x_cnt - 1) % (x_cnt - 1)
            ans[i] = 1 + count(z)
    # print(i, z, ans[i])
    bp *= 2
    bp %= x_cnt + 1
    if x_cnt != 1:
        bm *= 2
        bm %= x_cnt - 1

print(*ans, sep='\n')
