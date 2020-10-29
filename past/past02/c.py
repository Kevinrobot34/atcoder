n = int(input())
s = [list(input()) for _ in range(n)]

for i in reversed(range(n - 1)):
    for j in range(n - 1 - i, n + i):
        if ''.join(s[i + 1][j - 1:j + 2]).count('X') >= 1:
            s[i][j] = 'X'

for si in s:
    print(''.join(si))
