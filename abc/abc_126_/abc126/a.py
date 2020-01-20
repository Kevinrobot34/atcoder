n, k = map(int, input().split())
s = input()

t = ''
for i in range(n):
    if i+1 == k:
        t += s[i].lower()
    else:
        t += s[i]

print(t)
