from collections import Counter
l, r = map(int, input().split())
l_size = list(map(int, input().split()))
r_size = list(map(int, input().split()))

l_size_cnt = Counter(l_size)
r_size_cnt = Counter(r_size)

ans = 0
for k, v in l_size_cnt.items():
    if k in r_size_cnt:
        ans += min(r_size_cnt[k], v)

print(ans)
