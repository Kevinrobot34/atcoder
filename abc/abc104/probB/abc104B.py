import re

s = input()

flag = 0
for i in range(2, len(s)-1):
    if s[i] == 'C':
        flag += 1

if s[0] == 'A' and flag == 1 and len(re.findall('[A-Z]', s)) == 2:
    print('AC')
else:
    print('WA')
