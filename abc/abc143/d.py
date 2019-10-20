from bisect import bisect_left, bisect_right
n = int(input())
l = list(map(int, input().split()))
l.sort()
# print(l)

ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        idx = bisect_left(l, l[i] + l[j])
        ans += idx - (j+1)

print(ans)
