n = int(input())
a = list(map(int, input().split()))

b = [0] * (max(a) + 1)
# b[i] = (aの要素がiであるような数)
for i in range(n):
    b[a[i]] += 1

ans = 0
for i in range(1, len(b)):
    if b[i] > 0:
        if b[i] == 1:
            ans += 1
        # print(i, ans)
        for j in range(len(b)):
            if i * j >= len(b):
                break
            b[i * j] = 0

print(ans)
