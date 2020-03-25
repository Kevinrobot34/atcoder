from collections import defaultdict
n = int(input())
s = tuple(input() for _ in range(n))

cnt_dict = defaultdict(int)
cnt_max = 0
for si in s:
    cnt_dict[si] += 1
    cnt_max = max(cnt_max, cnt_dict[si])

ans = [key for key in cnt_dict if cnt_dict[key] == cnt_max]
ans.sort()
print(*ans, sep='\n')
