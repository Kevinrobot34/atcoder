s = input()

cand = []
for i in range(len(s)):
    cand.append(s)
    s = s[1:] + s[0]

cand.sort()
print(cand[0])
print(cand[-1])
