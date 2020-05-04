from collections import defaultdict
n = int(input())
a = tuple(map(int, input().split()))

ans = 0
cnt = defaultdict(int)
for j in range(n):
    y = j - a[j]
    x = j + a[j]
    ans += cnt[y]
    cnt[x] += 1

print(ans)
