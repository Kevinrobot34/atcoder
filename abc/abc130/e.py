n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [[0] * 2005 for _ in range(2005)]
