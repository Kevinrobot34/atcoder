n = int(input())
cnt_r = cnt_b = 0
for _ in range(n):
    s = input()
    cnt_r += s.count('R')
    cnt_b += s.count('B')

if cnt_r > cnt_b:
    ans = 'TAKAHASHI'
elif cnt_r == cnt_b:
    ans = 'DRAW'
else:
    ans = 'AOKI'

print(ans)
