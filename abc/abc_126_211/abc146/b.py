n = int(input())
s = input()

t = [chr(ord('A') + (ord(s[i]) - ord('A') + n) % 26) for i in range(len(s))]
ans = ''.join(t)
print(ans)
