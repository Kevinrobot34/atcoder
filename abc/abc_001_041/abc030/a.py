a, b, c, d = map(int, input().split())
if b * c > a * d:
    ans = 'TAKAHASHI'
elif b * c == a * d:
    ans = 'DRAW'
else:
    ans = 'AOKI'
print(ans)
