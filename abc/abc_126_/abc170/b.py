x, y = map(int, input().split())

if y % 2 == 0:
    if y // 2 - x >= 0 and 2 * x - y // 2 >= 0:
        ans = 'Yes'
    else:
        ans = 'No'
else:
    ans = 'No'

print(ans)
