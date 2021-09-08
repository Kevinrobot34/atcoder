from itertools import permutations

n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for p in permutations(range(1, n)):
    x = t[0][p[0]]
    for i in range(len(p) - 1):
        x += t[p[i]][p[i + 1]]
    x += t[p[-1]][0]
    if x == k:
        ans += 1

print(ans)
