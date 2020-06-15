from itertools import combinations
n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]


def area(i, j, k):
    x1 = p[j][0] - p[i][0]
    y1 = p[j][1] - p[i][1]
    x2 = p[k][0] - p[i][0]
    y2 = p[k][1] - p[i][1]
    return abs(x1 * y2 - x2 * y1)


ans = 0
for i, j, k in combinations(range(n), r=3):
    a = area(i, j, k)
    # print(i, j, k, a)
    if a > 0 and a % 2 == 0:
        ans += 1

print(ans)
