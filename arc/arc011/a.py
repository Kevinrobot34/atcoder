m, n, N = map(int, input().split())

ans = N
while N >= m:
    ans += (N // m) * n
    N = N % m + (N // m) * n

print(ans)
