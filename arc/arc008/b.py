from collections import Counter
n, m = map(int, input().split())
name = Counter(list(input()))
kit = Counter(list(input()))

is_possible = True
for s in name:
    if s not in kit:
        is_possible = False

if is_possible:
    ans = 0
    for s in name:
        ans = max(ans, (name[s] + kit[s] - 1) // kit[s])
else:
    ans = -1

print(ans)
