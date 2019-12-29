x = int(input())
for i in range(1, 1000):
    if i**4 == x:
        ans = i
        break

print(ans)
