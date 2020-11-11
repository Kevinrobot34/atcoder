n, q = map(int, input().split())

data = [['N'] * n for _ in range(n)]
for _ in range(q):
    s = input()
    if s[0] == '1':
        _, a, b = map(int, s.split())
        a -= 1
        b -= 1
        data[a][b] = 'Y'
    elif s[0] == '2':
        _, a = map(int, s.split())
        a -= 1
        for i in range(n):
            if data[i][a] == 'Y' and i != a:
                data[a][i] = 'Y'
    elif s[0] == '3':
        _, a = map(int, s.split())
        a -= 1
        fl = [i for i in range(n) if data[a][i] == 'Y']
        for i in fl:
            for j in range(n):
                if data[i][j] == 'Y' and j != a:
                    data[a][j] = 'Y'

for data_i in data:
    print(''.join(data_i))
