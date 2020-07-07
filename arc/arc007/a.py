x = input()
s = input()
ans = ''.join(filter(lambda si: si != x, list(s)))
print(ans)
