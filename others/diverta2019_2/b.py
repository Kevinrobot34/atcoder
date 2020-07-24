from collections import defaultdict
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

cnt = defaultdict(int)
cnt[(0, 0)] = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        cnt[(points[i][0] - points[j][0], points[i][1] - points[j][1])] += 1

# print(cnt)
ans = n - max(cnt.values())
print(ans)
