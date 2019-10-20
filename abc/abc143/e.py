import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())

INF = 10 ** 10

d = [[INF] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

# print()
# print(*d, sep='\n')

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if d[i][j] <= l:
            d[i][j] = 1
        else:
            d[i][j] = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

# print()
# print(*d, sep='\n')

q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1

    if d[s][t] == INF:
        print(-1)
    else:
        print(d[s][t]-1)
