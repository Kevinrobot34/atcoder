n = int(input())
flowers = set()
ans = 0
for _ in range(n):
    a = int(input())
    if a in flowers:
        ans += 1
    flowers.add(a)

print(ans)
