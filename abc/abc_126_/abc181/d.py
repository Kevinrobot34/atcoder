from itertools import permutations
from collections import Counter
s = input()

cand = dict(Counter(s))
for k, v in cand.items():
    cand[k] = min(3, v)

ss = ''.join(k * v for k, v in cand.items())
flag = False
for t in permutations(ss, min(3, len(s))):
    # print(t)
    if int(''.join(t)) % 8 == 0:
        flag = True
        break

ans = 'Yes' if flag else 'No'
print(ans)
