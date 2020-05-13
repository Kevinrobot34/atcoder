w = input()
ans = ''
for i in range(len(w)):
    if w[i] not in ['a', 'i', 'u', 'e', 'o']:
        ans += w[i]
print(ans)
