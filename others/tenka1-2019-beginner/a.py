a, b, c = map(int, input().split())
if a < c < b or b < c < a:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
