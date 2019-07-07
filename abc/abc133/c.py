l, r = map(int, input().split())

x = [i % 2019 for i in range(l, min(r+1, l+2019+1))]
x.sort()

ans = 2019
for i in range(len(x)):
    for j in range(i+1, len(x)):
        ans = min(ans, (x[i] * x[j]) % 2019)

print(ans)
