s = input()
s = s.replace("LR", "L R").split()

ans = []
for ss in s:
    a = b = 0
    c = d = 0
    for i in range(len(ss)):
        if ss[i] == 'R':
            a += 1
        else:
            b += 1

    if a % 2 == 0:
        c += a // 2
        d += a // 2
    else:
        c += (a + 1) // 2
        d += (a - 1) // 2

    if b % 2 == 0:
        c += b // 2
        d += b // 2
    else:
        c += (b - 1) // 2
        d += (b + 1) // 2

    ans += [0]*(a-1) + [c, d] + [0]*(b-1)

print(' '.join([str(ai) for ai in ans]))
