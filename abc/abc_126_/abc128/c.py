n, m = map(int, input().split())
switch = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

ans = 0
for bits in range(1<<n):
    all_on = True
    for i in range(m):
        pow = 0
        for j in range(1, switch[i][0]+1):
            pow += (bits >> (switch[i][j]-1)) & 1
        if pow % 2 != p[i]:
            all_on = False
            break

    if all_on:
        # print(''.join([str((bits>>i)&1) for i in range(n)]))
        ans += 1

print(ans)
