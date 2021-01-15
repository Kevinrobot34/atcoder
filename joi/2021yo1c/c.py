n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for ai in a:
    for bj in b:
        if ai <= bj:
            ans += 1

print(ans)
