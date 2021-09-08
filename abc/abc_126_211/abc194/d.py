n = int(input())
ans = 0
for k in range(1, n):
    ans = ans + 1 + k / (n - k)
print(ans)
