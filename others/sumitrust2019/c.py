x = int(input())

x1 = x // 100
x0 = x % 100

cnt = 0
for i in reversed(range(1, 6)):
    cnt += x0 // i
    x0 %= i

ans = int(x1 >= cnt)
print(ans)
