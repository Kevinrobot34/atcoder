n = int(input())
s1 = input()
s2 = input()

for i in range(n):
    c1 = s1[i]
    c2 = s2[i]
    if 'A' <= c1 <= 'Z':
        if 'A' <= c2 <= 'Z':
            if c1 != c2:
                s1 = s1.replace(c2, c1)
                s2 = s2.replace(c2, c1)
        else:
            # c2 is digit

            s1 = s1.replace(c1, c2)
            s2 = s2.replace(c1, c2)
    else:
        # c1 is digit
        if 'A' <= c2 <= 'Z':
            s1 = s1.replace(c2, c1)
            s2 = s2.replace(c2, c1)

ans = 1
d = set()
for i in range(n):
    if 'A' <= s1[i] <= 'Z' and s1[i] not in d:
        d.add(s1[i])
        if i == 0:
            ans *= 9
        else:
            ans *= 10

print(ans)
