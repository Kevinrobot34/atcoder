from bisect import bisect_right

a, b, q = map(int, input().split())
INF = 10**11
s = [-INF] + [int(input()) for _ in range(a)] + [INF]
t = [-INF] + [int(input()) for _ in range(b)] + [INF]

for _ in range(q):
    x = int(input())

    si = bisect_right(s, x)
    ti = bisect_right(t, x)

    ans = INF * 10
    for ss in [s[si-1], s[si]]:
        for tt in [t[ti-1], t[ti]]:
            ans = min(ans,
                      abs(x - ss) + abs(ss - tt),
                      abs(x - tt) + abs(tt - ss))
    print(ans)
