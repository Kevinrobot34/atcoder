n = int(input())
s = input()

t = 'b'
ans = -1
i = 0
while len(t) <= len(s):
    if t == s:
        ans = i
        break
    i += 1
    if i % 3 == 1:
        t = 'a' + t + 'c'
    elif i % 3 == 2:
        t = 'c' + t + 'a'
    else:
        t = 'b' + t + 'b'

print(ans)
