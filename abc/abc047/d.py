n, t = map(int, input().split())
a = list(map(int, input().split()))

a_max = [a[-1]] * n
for i in reversed(range(n-1)):
    a_max[i] = max(a[i], a_max[i+1])

a_min = [a[0]] * n
a_diff_max = 0
for i in range(1, n):
    a_min[i] = min(a[i], a_min[i-1])
    a_diff_max = max(a_diff_max, a_max[i] - a_min[i-1])

a_min_max = set()
for i in range(n-1):
    if a_max[i+1] - a_min[i] == a_diff_max:
        a_min_max.add((a_max[i+1], a_min[i]))

ans = len(a_min_max)
print(ans)
