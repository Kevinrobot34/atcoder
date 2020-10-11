import random
n = 13
m = 26
cand = 'abcdefghijklmnopqrstuvwxyz'
s = [
    'abcdefghijklm',
]

used_set = set()
for i in range(n - 1):
    used_set.add(s[0][i:i + 2])
    # used_set.add(s[1][i:i + 2])
# for i in range(n):
#     used_set.add(s[0][i] + s[1][i])


def check(i, j, c):
    ver = (s[i - 1][j] + c) in used_set
    if j == 0:
        return not ver
    else:
        hol = (s[i][j - 1] + c) in used_set
        return not (ver or hol)


for i in range(1, n):
    s.append('')
    for j in range(n):
        for k in random.sample(list(range(m)), m):
            if check(i, j, cand[k]):
                print(i, j, cand[k])
                used_set.add(s[i - 1][j] + cand[k])
                if j != 0:
                    used_set.add(s[i][j - 1] + cand[k])
                s[i] += cand[k]
                break

used_set
print(n)
print(*s, sep='\n')
