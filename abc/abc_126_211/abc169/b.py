n = int(input())
a = list(map(int, input().split()))
a.sort()

MAX = 10**18
ans = 1

for i in range(n):
    ans *= a[i]
    if ans > MAX:
        ans = -1
        break

print(ans)
