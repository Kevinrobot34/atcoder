n = int(input())
ans = min((n // 10) * 100 + (n % 10) * 15, (n // 10 + 1) * 100)
print(ans)
