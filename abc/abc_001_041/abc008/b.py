from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
cnt_s = Counter(s)

cnt_max = max(cnt_s.values())
for k, v in cnt_s.items():
    if v == cnt_max:
        ans = k
        break

print(ans)
