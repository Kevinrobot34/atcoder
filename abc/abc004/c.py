n = int(input())

n0 = n % 5
n1 = (n // 5) % 6

s = list("123456123456")[n1:n1 + 6]
# print(s)
for i in range(n0):
    s[i], s[i + 1] = s[i + 1], s[i]

ans = ''.join(s)
print(ans)
