from collections import Counter
a = input()
n = len(a)

cnt = Counter(a)
ans = n * (n - 1) // 2 - sum(m * (m - 1) // 2 for m in cnt.values()) + 1
print(ans)
