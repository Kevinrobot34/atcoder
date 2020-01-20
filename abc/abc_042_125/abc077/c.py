from bisect import bisect_left, bisect_right

n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
c = sorted(map(int, input().split()))

ans = 0
for i in range(len(b)):
    ai = bisect_left(a, b[i])
    ci = bisect_right(c, b[i])
    # print(i, ai, ci)
    ans += ai * (n - ci)

print(ans)
