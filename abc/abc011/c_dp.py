MAX = 1000
n = int(input())
ng_list = [int(input()) for _ in range(3)]

cnt = [0] * 305
for ng_i in ng_list:
    cnt[ng_i] = MAX
cnt[n + 1] = cnt[n + 2] = MAX

for i in reversed(range(n)):
    if cnt[i] == MAX:
        continue
    cnt[i] = min(cnt[i + 1], cnt[i + 2], cnt[i + 3]) + 1

ans = "YES" if cnt[0] <= 100 else "NO"
print(ans)
