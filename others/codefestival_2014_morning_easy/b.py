n = int(input())
if ((n - 1) // 20) % 2 == 0:
    ans = (n - 1) % 20 + 1
else:
    ans = 20 - (n - 1) % 20
print(ans)
