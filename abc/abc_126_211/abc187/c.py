n = int(input())

s1 = set()
s2 = set()
for _ in range(n):
    si = input()
    if si[0] == '!':
        s2.add(si[1:])
    else:
        s1.add(si)

s = s1 & s2
if len(s) == 0:
    ans = 'satisfiable'
else:
    ans = list(s)[0]
print(ans)
