n, m = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)
a.append(n + 1)
a.sort()

a_diff = [a[i + 1] - a[i] - 1 for i in range(m + 1) if a[i + 1] != a[i] + 1]
# print(a)
# print(a_diff)

if len(a_diff) > 0:
    k = min(a_diff)
    ans = sum((x + k - 1) // k for x in a_diff)
else:
    ans = 0

print(ans)
