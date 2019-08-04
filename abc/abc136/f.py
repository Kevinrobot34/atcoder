MOD = 998244353
n = int(input())
p = []
xs = []
for i in range(n):
    x, y = map(int, input().split())



p.sort(key=lambda x: x[0])
print(p)
