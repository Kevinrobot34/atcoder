def transform(s):
    if s[0] == 'B':
        return -(int(s[1]) - 1)
    else:
        return int(s[0])


s, t = input().split()
ans = abs(transform(t) - transform(s))
print(ans)
