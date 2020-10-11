n = int(input())
p = list(map(int, input().split()))

s = set()
ans = 0
for i in range(n):
    s.add(p[i])
    while ans in s:
        ans += 1
    print(ans)
