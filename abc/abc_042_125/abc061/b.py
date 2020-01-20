n, m = map(int, input().split())

edges = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a] += 1
    edges[b] += 1

print(*edges, sep='\n')
