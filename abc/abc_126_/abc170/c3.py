x, n = map(int, input().split())
p = list(map(int, input().split()))
p = set(p)

ans = 0
for i in range(102):
    if i not in p and abs(ans - x) > abs(i - x):
        ans = i

print(ans)
