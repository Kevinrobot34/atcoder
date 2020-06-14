n = int(input())
a = list(map(int, input().split()))
a.sort()

cnt = [0] * (a[-1] + 1)
for i in range(n):
    cnt[a[i]] += 1

ans = 0
for i in range(1, a[-1] + 1):
    if cnt[i] > 0:
        if cnt[i] == 1:
            ans += 1
        for j in range(2, a[-1] + 1):
            na = i * j
            if na <= a[-1]:
                cnt[na] = 0
            else:
                break

print(ans)
