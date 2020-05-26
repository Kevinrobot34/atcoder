n = int(input())
a, b = map(int, input().split())

if a == b:
    if n % (a + 1) == 0:
        ans = 'Aoki'
    else:
        ans = 'Takahashi'
elif a > b:
    ans = 'Takahashi'
else:
    if n <= a:
        ans = 'Takahashi'
    else:
        ans = 'Aoki'

print(ans)
