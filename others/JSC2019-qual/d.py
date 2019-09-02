n = int(input())

for i in range(1, n):
    ans = []
    for j in range(n-i):
        # print(i, j)
        if j % 2 == 0:
            ans.append(1)
        else:
            ans.append(2 + (i-1)//2)
    print(' '.join([str(ansi) for ansi in ans]))
