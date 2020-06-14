n, k = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(k):
    b = [0] * (n + 2)
    for i in range(n):
        b[max(0, i - a[i])] += 1
        b[min(n + 1, i + a[i] + 1)] -= 1
    a[0] = b[0]
    cnt = a[0]
    for i in range(1, n):
        a[i] = a[i - 1] + b[i]
        cnt += a[i]

    # print(*a)
    if cnt == n**2:
        break

print(*a)
