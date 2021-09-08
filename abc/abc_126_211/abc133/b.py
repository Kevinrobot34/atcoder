import math
n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]

def dist(a, b):
    return math.sqrt(sum([(a[i] - b[i])**2 for i in range(d)]))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        y = x[i]
        z = x[j]
        w = dist(y, z)
        # print(w, int(w), w == int(w))
        if w == int(w):
            ans += 1

# print(x)
print(ans)
