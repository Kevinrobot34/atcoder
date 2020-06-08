n, k = map(int, input().split())
t = [int(input()) for _ in range(n)]

ans = -1
s = t[0] + t[1]
for i in range(2, n):
    s += t[i]
    if s < k:
        ans = i + 1
        break
    s -= t[i - 2]
print(ans)
