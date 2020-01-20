n = int(input())
s = input()

inv = {'S': 'W', 'W': 'S'}
def check(t):
    for i in range(2, n):
        if t[i-1] == 'S':
            if s[i-1] == 'o':
                t.append(t[i-2])
            else:
                t.append(inv[t[i-2]])
        else:
            if s[i-1] == 'o':
                t.append(inv[t[i-2]])
            else:
                t.append(t[i-2])

    if t[0] == 'S':
        if s[0] == 'o' and t[1] != t[-1]:
            return "-1"
        elif s[0] == 'x' and t[1] == t[-1]:
            return "-1"
    else:
        if s[0] == 'o' and t[1] == t[-1]:
            return "-1"
        elif s[0] == 'x' and t[1] != t[-1]:
            return "-1"

    if t[-1] == 'S':
        if s[-1] == 'o' and t[0] != t[-2]:
            return "-1"
        elif s[-1] == 'x' and t[0] == t[-2]:
            return "-1"
    else:
        if s[-1] == 'o' and t[0] == t[-2]:
            return "-1"
        elif s[-1] == 'x' and t[0] != t[-2]:
            return "-1"

    return ''.join(t)

ans = "-1"
for t in [['S', 'S'], ['S', 'W'], ['W', 'S'], ['W', 'W']]:
    res = check(t)
    if res != "-1":
        ans = res
        break

print(ans)
