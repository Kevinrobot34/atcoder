from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
# print(a)

# a_cnt[k] = (num of a[i] where a[i] >= k)
a_cnt = [0] * (2 * a[-1] + 5)
for ai in a:
    a_cnt[ai] += 1
for i in reversed(range(len(a_cnt) - 1)):
    a_cnt[i] += a_cnt[i + 1]

# a_cs[i] = sum(a[n-i:])
a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[n - 1 - i]


def check(x):
    # M回の握手の幸福度の最小値をx以上にできるか
    # つまり、M回の任意の握手の幸福度をx以上にできるか
    cnt = 0
    for ai in a:
        if x >= ai:
            idx = a_cnt[x - ai]
        else:
            idx = n
        cnt += idx
    return cnt >= m


lb = 1  # True
ub = 2 * a[-1] + 3  # False
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        lb = mid
    else:
        ub = mid

# print(lb)

ans = 0
cnt = 0
for ai in a:
    if lb >= ai:
        idx = a_cnt[lb - ai]
    else:
        idx = n
    ans += ai * idx + a_cs[idx]
    cnt += idx
ans -= lb * (cnt - m)
print(ans)
