s = input()

if s == 'a' or s == 'z' * 20:
    ans = 'NO'
elif len(set(s)) > 1:
    ans = s[1:] + s[0]  # cyclic
elif len(s) == 1:
    ans = chr(ord(s[0]) - 1) + 'a'
else:
    # len(s) != 1 and len(set(s)) == 1
    if s[0] == 'a':
        ans = chr(ord('a') + len(s) - 1)
    elif s[0] == 'z':
        ans = s[:-1] + chr(ord(s[0]) - 1) + 'a'
    else:
        ans = s[:-2] + chr(ord(s[0]) - 1) + chr(ord(s[0]) + 1)

print(ans)
