from itertools import permutations
import math

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]

ans = cnt = 0
for perm in permutations(range(n)):
    dist = 0
    for i in range(1, n):
        dist += math.sqrt((p[perm[i]][0] - p[perm[i - 1]][0])**2 +
                          (p[perm[i]][1] - p[perm[i - 1]][1])**2)

    # print(perm, dist)
    ans += dist
    cnt += 1

ans /= cnt
print(ans)
