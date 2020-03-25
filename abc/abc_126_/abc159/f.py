n, s = map(int, input().split())
a = tuple(map(int, input().split()))
MOD = 998244353

dp1 = [[0] * (s + 1) for _ in range(n + 1)]
dp2 = [[0] * (s + 1) for _ in range(n + 1)]
dp3 = [[0] * (s + 1) for _ in range(n + 1)]
