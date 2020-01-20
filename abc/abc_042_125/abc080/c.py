n = int(input())
f = [list(map(int, input().split())) for i in range(n)]
p = [list(map(int, input().split())) for i in range(n)]

ans = - 10**10
for i in range(1, 1<<10):
    tmp_ans = 0
    for j in range(n):
        c = 0
        for k in range(10):
            if f[j][k] == 1 and (i >> k) & 1 == 1:
                c += 1
        tmp_ans += p[j][c]
    ans = max(ans, tmp_ans)

print(ans)
