n, m, q = map(int, input().split())

train = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    train[l+1][r+1] += 1

for i in range(0, n+1):
    for j in range(1, n+1):
        train[i][j] = train[i][j] + train[i][j-1]
for j in range(0, n+1):
    for i in range(1, n+1):
        train[i][j] = train[i][j] + train[i-1][j]


for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    print(train[r+1][r+1] - train[l][r+1] - train[r+1][l] + train[l][l])
