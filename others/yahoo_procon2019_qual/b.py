cnt = {1: 0, 2: 0, 3: 0, 4: 0}
for _ in range(3):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1

ans = 'YES'
for k, v in cnt.items():
    if v > 2:
        ans = 'NO'
        break

print(ans)
