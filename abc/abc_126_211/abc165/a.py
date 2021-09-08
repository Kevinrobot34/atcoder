k = int(input())
a, b = map(int, input().split())
if b % k == 0:
    ans = 'OK'
elif a % k == 0:
    ans = 'OK'
elif (b // k) - (a // k) > 0:
    ans = 'OK'
else:
    ans = 'NG'

print(ans)
