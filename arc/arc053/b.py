from collections import Counter
s = input()
n = len(s)

cnt = Counter(s)
k = Counter(v % 2 for v in cnt.values())

if k[1] == 0:
    ans = n
else:
    ans = ((n - k[1]) // (2 * k[1])) * 2 + 1

print(ans)
