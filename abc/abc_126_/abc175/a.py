s = input()

if s in ['SSS']:
    ans = 0
elif s in ['SSR', 'SRS', 'RSS', 'RSR']:
    ans = 1
elif s in ['SRR', 'RRS']:
    ans = 2
else:
    ans = 3

print(ans)
