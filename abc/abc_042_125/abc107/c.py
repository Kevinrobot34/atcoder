from bisect import bisect_left

n, k = map(int, input().split())
x = list(map(int, input().split()))

si = bisect_left(x, 0)

ans = (x[-1] - x[0]) * 2
if si + k - 1 < len(x):
    ans = min(ans, x[si + k - 1])
if si - k >= 0:
    ans = min(ans, abs(x[si - k]))

for i in range(n):
    tmp_ans = 0
    if i < si and i + k -1 < len(x):
        tmp_ans = abs(x[i]) * 2 + x[i + k - 1]
        ans = min(ans, tmp_ans)
    elif i >= si and i - k + 1 >= 0:
        tmp_ans = x[i] * 2 + abs(x[i - k + 1])
        ans = min(ans, tmp_ans)

print(ans)
