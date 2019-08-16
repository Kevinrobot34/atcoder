from operator import itemgetter
n, m = map(int, input().split())
a = list(map(int, input().split()))
op = [list(map(int, input().split())) for _ in range(m)]
op.sort(key=itemgetter(1), reverse=True)
a.sort()

idx = 0
ans = 0
for i in range(n):
    if idx < m and op[idx][1] > a[i]:
        ans += op[idx][1]
    else:
        ans += a[i]

    if idx < m and op[idx][0] > 1:
        op[idx][0] -= 1
    else:
        idx += 1

print(ans)
