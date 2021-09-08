from bisect import bisect_left, bisect_right
n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
for j in range(n):
    for k in range(j + 1, n):
        if l[j] == l[k]:
            continue

        ans += max(bisect_left(l, l[j]) - bisect_right(l, l[k] - l[j]), 0)

print(ans)
