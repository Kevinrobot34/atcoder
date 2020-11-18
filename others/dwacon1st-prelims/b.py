import re
s = input()
s = s.replace('25', 'x')
s = re.sub(r'\d+', 'y', s)

ans = sum(len(si) * (len(si) + 1) // 2 for si in s.split('y'))
print(ans)
