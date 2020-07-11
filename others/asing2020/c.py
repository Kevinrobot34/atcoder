n = int(input())

ans = [0] * (n + 1)
for x in range(1, n + 1):
    if x**2 + x >= n:
        break
    for y in range(1, n + 1):
        if x**2 + y**2 + x * y + x + y >= n:
            break
        for z in range(1, n + 1):
            w = x**2 + y**2 + z**2 + x * y + y * z + z * x
            if w > n:
                break
            else:
                ans[w] += 1

for i in range(1, n + 1):
    print(ans[i])
