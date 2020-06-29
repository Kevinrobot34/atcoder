from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

ans = 0
cnt = defaultdict(int)
left = 0
for right in range(1, n + 1):
    cnt[a[right - 1]] += 1

    while left < right and cnt[a[right - 1]] == 2:
        cnt[a[left]] -= 1
        left += 1

    ans = max(ans, right - left)

print(ans)
