s, l, r = map(int, input().split())
if s < l:
    ans = l
elif s < r:
    ans = s
else:
    ans = r
print(ans)
