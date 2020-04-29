a = int(input())
b = int(input())
ans = min(abs(a - b), 10 + a - b, 10 + b - a)
print(ans)
