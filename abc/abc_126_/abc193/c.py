n = int(input())
ans = n
m = int(n**0.5) + 1
flag = [False] * m

for a in range(2, m):
    if flag[a]:
        continue

    c = a**2
    cnt = 0
    while c <= n:
        if c < m:
            flag[c] = True
        cnt += 1
        c *= a
    ans -= cnt

print(ans)
