from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1

k = list(d.keys())
v = list(d.values())

if len(k) == 1 and k[0] == 0:
    ans = "Yes"
elif n % 3 != 0:
    ans = "No"
elif len(k) == 2 and 0 in d and d[0] == n // 3:
    ans = "Yes"
elif len(k) == 3 and v[0] == v[1] == v[2] and k[0] ^ k[1] ^ k[2] == 0:
    ans = "Yes"
else:
    ans = "No"

print(ans)
