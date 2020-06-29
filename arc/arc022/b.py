from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

ans = 0
cnt = defaultdict(int)
right = 1
cnt[a[0]] += 1
for left in range(n):
    while right < n and cnt[a[right]] == 0:
        cnt[a[right]] += 1
        right += 1

    ans = max(ans, right - left)
    cnt[a[left]] -= 1

print(ans)
