a = int(input())
ans = 0
for i in range(1, a):
    ans = max(ans, i * (a - i))
print(ans)
