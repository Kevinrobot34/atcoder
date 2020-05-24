s = input()
x = s.replace('<>', '<|>').split('|')


def func(t):
    c1 = t.count('>')
    c2 = len(t) - c1
    return list(reversed(range(1, c1 + 1))) + list(range(c2 + 1))


a = func(x[0])
for i in range(1, len(x)):
    ai = func(x[i])
    a[-1] = max(a[-1], ai[0])
    a.extend(ai[1:])

# print(a)
ans = sum(a)
print(ans)
