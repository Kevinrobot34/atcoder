import math

n = int(input())
a = list(map(int, input().split()))

if max(a) > 0:
    m = math.ceil(math.log2(max(a)))
else:
    m = 1

ans = n
index = 0
cs = [[0 for i in range(m)] for i in range(n+1)]
bit = [0 for i in range(m)]
for i in range(n):
    for j in range(m):
        cs[i+1][j] = cs[i][j] + ((a[i]>>j)&1)

    bit = [cs[i+1][j] - cs[index][j] for j in range(m)]
    if max(bit) >= 2:
        while max(bit) >= 2:
            k = max(i - index - 1, 0)
            ans += k
            index += 1
            bit = [cs[i+1][j] - cs[index][j] for j in range(m)]

    # print("{:2d} {:2d}".format(i, index), ans, "".join([str((a[i]>>j)&1) for j in reversed(range(m))]))

k = max(n - index - 1, 0)
ans += k * (k+1) // 2
# print(cs)
print(ans)
