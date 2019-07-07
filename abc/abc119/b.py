n = int(input())

rate_btc = 380000.0

ans = 0.0
for _ in range(n):
    x, u = input().split()
    x = float(x)
    if u == "BTC":
        x = x * rate_btc

    ans += x

print(ans)
