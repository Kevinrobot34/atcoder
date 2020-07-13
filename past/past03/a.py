s = input()
t = input()

if s == t:
    ans = 'same'
elif s.lower() == t.lower():
    ans = 'case-insensitive'
else:
    ans = 'different'

print(ans)
