n = int(input())
s = input()

l = []
for i in range(n):
    l.append(s[i])
    if len(l) >= 3 and ''.join(l[-3:]) == 'fox':
        l.pop()
        l.pop()
        l.pop()

print(len(l))
