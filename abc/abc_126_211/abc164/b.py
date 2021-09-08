a, b, c, d = map(int, input().split())
ans = 'No'
while a > 0 and c > 0:
    if ans == 'No':
        c -= b
        ans = 'Yes'
    else:
        a -= d
        ans = 'No'

print(ans)
