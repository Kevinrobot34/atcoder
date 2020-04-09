n = int(input())
a, b = map(int, input().split())
k = int(input())
p = set(map(int, input().split()))

if len({a, b} | p) == k + 2:
    ans = 'YES'
else:
    ans = 'NO'

print(ans)
