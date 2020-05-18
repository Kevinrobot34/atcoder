s = input()
ans = ''.join(s[i] for i in range(len(s)) if s[i] in '0123456789')
print(ans)
