n = int(input())
a = list(map(int, input().split()))

a_cs = [0] * (n + 1)
for i in range(n):
    a_cs[i + 1] = a_cs[i] + a[i]

a_cs_cs = [0] * (n + 1)
for i in range(n):
    a_cs_cs[i + 1] = a_cs_cs[i] + a_cs[i + 1]

a_cs_maxi = 0
for i in range(n + 1):
    if a_cs_cs[a_cs_maxi] <= a_cs_cs[i]:
        a_cs_maxi = i

# print(a_cs)
# print(a_cs_cs)
# print(a_cs_maxi)
if a_cs_maxi == n:
    ans = max(a_cs_cs[a_cs_maxi], a_cs_cs[a_cs_maxi - 1] + max(a_cs))
else:
    ans = a_cs_cs[a_cs_maxi] + max(a_cs[:a_cs_maxi + 2])

print(ans)
