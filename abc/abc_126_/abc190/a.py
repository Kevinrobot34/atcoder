a, b, c = map(int, input().split())
if c == 0:
    ans = 'Takahashi' if a > b else 'Aoki'
else:
    ans = 'Aoki' if b > a else 'Takahashi'
print(ans)
