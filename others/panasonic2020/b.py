h, w = map(int, input().split())
if h == 1 or w == 1:
    ans = 1
else:
    ans = (h * w + 1) // 2
print(ans)
