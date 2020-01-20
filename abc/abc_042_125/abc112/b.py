n, t = map(int, input().split())

ans = 10**9
for i in range(n):
    ci, ti = map(int, input().split())
    if ti <= t:
        ans = min(ans, ci)

if ans == 10**9:
    print("TLE")
else:
    print(ans)
