w, h = map(int, input().split())
if h % (w - h) == 0:
    ans = "4:3"
else:
    ans = "16:9"

print(ans)
