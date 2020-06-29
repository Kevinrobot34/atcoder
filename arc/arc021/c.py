k = int(input())
n = int(input())
house = [tuple(map(int, input().split())) for _ in range(n)]


def check(x):
    # x円以下のものすべて増築した時に、k回を超えるかを判定する
    cnt = 0
    for ai, di in house:
        cnt += (x - ai) // di + 1
    return cnt >= k


lb = -1  # False
ub = 10**12  # True
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid

ans = 0
cnt = 0
for ai, di in house:
    if (ub - ai) % di == 0:
        m = (ub - ai) // di - 1
    else:
        m = (ub - ai) // di
    ans += ai * (m + 1) + di * m * (m + 1) // 2
    cnt += m + 1

ans += ub * (k - cnt)

print(ub)
print(ans)
