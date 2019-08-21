from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    for border in reversed(range(0, 3201, 400)):
        if a[i] >= border:
            d[border] += 1
            break

ans_min = ans_max = 0
if 3200 in d:
    if len(d) > 1:
        ans_min, ans_max = len(d)-1, len(d)-1+d[3200]
    else:
        ans_min, ans_max = 1, d[3200]
else:
    ans_min, ans_max = len(d), len(d)

print(ans_min, ans_max)
