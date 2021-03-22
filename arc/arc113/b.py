a, b, c = map(int, input().split())
a %= 10
x = [1, 1, 4, 4, 2, 1, 1, 4, 4, 2]
ans = pow(a, x[a] + pow(b, c, x[a]), 10)
print(ans)
