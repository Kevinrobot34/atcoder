n = int(input())
s = [input() for _ in range(n)]


def func(x):
    ret = []
    for i in range(len(x)):
        if len(ret) == 0:
            ret.append(x[i])
        else:
            if ret[-1] == '(' and x[i] == ')':
                ret.pop()
            else:
                ret.append(x[i])
    l = r = 0
    for i in range(len(ret)):
        if ret[i] == '(':
            l += 1
        else:
            r += 1
    return (r, l)  # ) (


t = []
for i in range(n):
    r, l = func(s[i])
    # print((r, l), '<-', s[i])
    if r + l == 0:
        continue
    t.append((r, l))
t.sort(key=lambda x: (x[0], -x[1]))
print(*t, sep='\n')

is_possible = True
if len(t) > 0:
    r, l = t[0]
    if r != 0:
        is_possible = False
    else:
        for i in range(1, len(t)):
            r_i, l_i = t[i]
            if r_i <= l:
                l -= r_i
                l += l_i
            else:
                is_possible = False
                break
        if l != 0:
            is_possible = False

ans = 'Yes' if is_possible else 'No'
print(ans)
