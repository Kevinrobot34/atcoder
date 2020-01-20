import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
s = list(map(int, input()))


def solve(x):
    if x <= m + 1:
        return [x - 1]
    for i in range(m, 0, -1):
        if s[x - 1 - i] == 0:
            cand = solve(x - i)
            if len(cand) != 0:
                cand.append(i)
                return cand

    return []


cnt1_continuous = 0
cnt = 0
for i in range(n + 1):
    if s[i] == 1:
        cnt += 1
        if i == n:
            cnt1_continuous = max(cnt1_continuous, cnt)
    else:
        cnt1_continuous = max(cnt1_continuous, cnt)
        cnt = 0

if cnt1_continuous >= m:
    print(-1)
else:
    print(*solve(len(s)))
