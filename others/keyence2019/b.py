def check(s):
    t = 'keyence'
    if s == t:
        return 'YES'
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if t == s[:i] + s[j:]:
                return 'YES'
    return 'NO'


s = input()
print(check(s))
