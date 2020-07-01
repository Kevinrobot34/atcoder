n = int(input())
m = 9
score = ['.' * m] + [input() for _ in range(n)]

ans = 0
for i in range(1, len(score)):
    for j in range(m):
        if score[i][j] == 'x':
            ans += 1
        elif score[i][j] == 'o' and score[i - 1][j] != 'o':
            ans += 1

print(ans)
