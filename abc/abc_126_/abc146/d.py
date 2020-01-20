import sys
input = sys.stdin.readline

n = int(input())
edge = {}
tree = [[] for i in range(n)]
color = [0] * (n - 1)
color_par = [-1] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    edge[(a, b)] = i

for i in range(n):
    c = 1
    for v_child in tree[i]:
        if c == color_par[i]:
            c += 1
        color[edge[(i, v_child)]] = c
        color_par[v_child] = c
        c += 1

print(max(color))
print(*color, sep='\n')
