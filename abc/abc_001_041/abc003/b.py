from collections import deque
s = input()
t = input()
c = 'atcoder'

is_possible = True
for i in range(len(s)):
    if s[i] == '@':
        if t[i] == '@':
            continue
        else:
            if t[i] not in c:
                is_possible = False
                break
    else:
        if t[i] == '@':
            if s[i] not in c:
                is_possible = False
                break
        else:
            if s[i] != t[i]:
                is_possible = False
                break

ans = 'You can win' if is_possible else 'You will lose'
print(ans)
