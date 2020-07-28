import re
n = int(input())
s = input()
k = int(input())

ans = re.sub(rf'[^{s[k-1]}]', '*', s)
print(ans)
