n = int(input())
s = [input() for _ in range(n)]
for i in range(n):
    print(''.join(s[n - 1 - j][i] for j in range(n)))
