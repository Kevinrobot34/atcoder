n, z, w = map(int, input().split())
a = list(map(int, input().split()))

ans = abs(a[-1] - w)
if n >= 2:
    ans = max(ans, abs(a[-1] - a[-2]))

print(ans)
