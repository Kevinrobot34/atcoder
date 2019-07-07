h, w = map(int, input().split())
s = ['.'*(w+2)] + ['.' + input() + '.' for i in range(h)] + ['.'*(w+2)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

ans = 0
for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j] == '.':
            continue
        c = 0
        for k in range(4):
            if s[i+d[k][0]][j+d[k][1]] == "#":
                c += 1
        if c == 0:
            ans = -1

if ans == -1:
    print("No")
else:
    print("Yes")
