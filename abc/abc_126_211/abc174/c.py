k = int(input())

x = 7 % k
s = set()
for i in range(k):
    if x % k == 0:
        ans = i + 1
        break
    if x in s:
        ans = -1
        break

    s.add(x)
    x = 10 * x + 7
    x %= k

print(ans)
