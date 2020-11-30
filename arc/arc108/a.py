s, p = map(int, input().split())

det = s**2 - 4 * p

if det >= 0 and int(det**0.5)**2 == det:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
