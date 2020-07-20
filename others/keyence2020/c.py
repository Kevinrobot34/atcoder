n, k, s = map(int, input().split())
ans = [s] * k + [s + 1 if s < 10**9 else s - 1] * (n - k)
print(*ans)
