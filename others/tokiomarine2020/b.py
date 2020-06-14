a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if v <= w:
    ans = 'NO'
else:
    if abs(a - b) <= (v - w) * t:
        ans = 'YES'
    else:
        ans = 'NO'

print(ans)
