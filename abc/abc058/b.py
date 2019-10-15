o = input()
e = input()

chars = [''] * (len(o) + len(e))
for i in range(len(chars)):
    if i % 2 == 0:
        chars[i] = o[i//2]
    else:
        chars[i] = e[i//2]

ans = ''.join(chars)
print(ans)
