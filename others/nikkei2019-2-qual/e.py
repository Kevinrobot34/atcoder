n, k = map(int, input().split())

if k == 1:
    for i in range(n):
        print(i + 1, 2 * n - i, 2 * n + 1 + i)
else:
    print(-1)
