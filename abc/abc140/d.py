n, k = map(int, input().split())
s = input()

b = 1
for i in range(1, n):
    if s[i] != s[i-1]:
        b += 1
# print(b)

b = max(1, b-2*k)

ans = n - b

print(ans)
