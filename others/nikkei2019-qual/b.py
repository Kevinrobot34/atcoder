n = int(input())
a = input()
b = input()
c = input()

ans = 0
for i in range(n):
    s = set([a[i], b[i], c[i]])
    ans += len(s) - 1

print(ans)
