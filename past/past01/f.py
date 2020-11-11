s = input()
t = []

i = 0
cnt = 0
for j in range(len(s)):
    if 'A' <= s[j] <= 'Z':
        cnt += 1
    if cnt % 2 == 0:
        t.append(s[i:j + 1])
        i = j + 1

t.sort(key=lambda x: x.lower())
ans = ''.join(t)
print(ans)
