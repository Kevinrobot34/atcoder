s = input()
t = int(input())
x = y = cnt = 0

for i in range(len(s)):
    if s[i] == 'L':
        x -= 1
    elif s[i] == 'R':
        x += 1
    elif s[i] == 'U':
        y += 1
    elif s[i] == 'D':
        y -= 1
    else:
        cnt += 1

if t == 1:
    ans = abs(x) + abs(y) + cnt
else:
    ans = abs(x) + abs(y)
    if ans >= cnt:
        ans -= cnt
    else:
        ans = (cnt - ans) % 2

print(ans)
