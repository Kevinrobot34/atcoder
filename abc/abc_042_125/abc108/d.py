import math
l = int(input())

# l -= 1
n = math.floor(math.log2(l)) + 1
edge = []
for i in range(1, n):
    edge.append((i, i+1, 0))
for j, i in enumerate(reversed(range(1, n))):
    edge.append((i, i+1, 2**j))

l2 = l - 2**(n-1)
c = 2**(n-1)
# print("test", c, l2)
while l2 > 0:
    l_mini = 1
    while l_mini * 2 <= l2:
        l_mini *= 2
    # print("test", c, l2, int(math.log2(l_mini)))
    edge.append((1, n-int(math.log2(l_mini)), c))
    l2 -= l_mini
    c += l_mini

print(n, len(edge))
for i in range(len(edge)):
    print(*edge[i])
