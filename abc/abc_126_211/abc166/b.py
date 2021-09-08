n, k = map(int, input().split())

cnt = [0] * (n + 1)
for _ in range(k):
    d = int(input())
    a = tuple(map(int, input().split()))
    for ai in a:
        cnt[ai] += 1

ans = 0
for i in range(1, n + 1):
    if cnt[i] == 0:
        ans += 1
print(ans)
