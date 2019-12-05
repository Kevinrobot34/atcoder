n = int(input())

ans = -1
for i in range(1, 50000):
    if int(i * 1.08) == n:
        ans = i
        break

if ans == -1:
    print(":(")
else:
    print(ans)
