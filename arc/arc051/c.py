from heapq import heappush, heappop, heapify
MOD = 10**9 + 7
n, a, b = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

if a > 1:
    x_max = x[-1]
    heapify(x)
    while b > 0 and x[0] * a < x_max:
        x_0 = heappop(x)
        heappush(x, x_0 * a)
        b -= 1
    x.sort()

    for i in range(n):
        if i < b % n:
            x[i] = (x[i] * pow(a, b // n, MOD) * a) % MOD
        else:
            x[i] = (x[i] * pow(a, b // n, MOD)) % MOD

    for i in range(n):
        print(x[(i + b % n) % n])
else:
    for i in range(n):
        print(x[i] % MOD)
